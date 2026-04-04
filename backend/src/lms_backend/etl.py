"""ETL pipeline: fetch data from the autochecker API and load it into the database.

The autochecker dashboard API provides two endpoints:
- GET /api/items — lab/task catalog
- GET /api/logs  — anonymized check results (supports ?since= and ?limit= params)

Both require HTTP Basic Auth (email + password from settings).
"""

from datetime import datetime

import httpx
from pydantic import BaseModel
from sqlmodel import col, select, func
from sqlmodel.ext.asyncio.session import AsyncSession

from lms_backend.models.interaction import InteractionLog
from lms_backend.models.item import ItemRecord
from lms_backend.models.learner import Learner
from lms_backend.settings import settings


# ---------------------------------------------------------------------------
# API response schemas
# ---------------------------------------------------------------------------


class ApiItem(BaseModel):
    type: str
    title: str
    lab: str
    task: str | None = None


class ApiLog(BaseModel):
    id: int
    student_id: str
    lab: str
    task: str | None = None
    group: str = ""
    score: float | None = None
    passed: int | None = None
    total: int | None = None
    submitted_at: str


class ApiLogsPage(BaseModel):
    logs: list[ApiLog]
    has_more: bool = False


# ---------------------------------------------------------------------------
# Extract — fetch data from the autochecker API
# ---------------------------------------------------------------------------


async def fetch_items() -> list[ApiItem]:
    """Fetch the lab/task catalog from the autochecker API."""
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.get(
            f"{settings.autochecker_api_url}/api/items",
            auth=(settings.autochecker_email, settings.autochecker_password),
        )
        resp.raise_for_status()
        return [ApiItem.model_validate(item) for item in resp.json()]


async def fetch_logs(since: datetime | None = None) -> list[ApiLog]:
    """Fetch check results from the autochecker API with pagination."""
    all_logs: list[ApiLog] = []

    async with httpx.AsyncClient(timeout=60) as client:
        cursor = since
        while True:
            params: dict[str, str | int] = {"limit": 500}
            if cursor is not None:
                params["since"] = cursor.isoformat()

            resp = await client.get(
                f"{settings.autochecker_api_url}/api/logs",
                params=params,
                auth=(settings.autochecker_email, settings.autochecker_password),
            )
            resp.raise_for_status()
            page = ApiLogsPage.model_validate(resp.json())

            all_logs.extend(page.logs)

            if not page.has_more or not page.logs:
                break

            cursor = datetime.fromisoformat(page.logs[-1].submitted_at)

    return all_logs


# ---------------------------------------------------------------------------
# Load — insert fetched data into the local database
# ---------------------------------------------------------------------------


async def load_items(items: list[ApiItem], session: AsyncSession) -> int:
    """Load items (labs and tasks) into the database."""
    created = 0
    lab_map: dict[str, ItemRecord] = {}

    # Process labs first
    for item in items:
        if item.type != "lab":
            continue
        existing = (
            await session.exec(
                select(ItemRecord).where(
                    ItemRecord.type == "lab", ItemRecord.title == item.title
                )
            )
        ).first()
        if existing:
            lab_map[item.lab] = existing
        else:
            record = ItemRecord(type="lab", title=item.title)
            session.add(record)
            await session.flush()
            lab_map[item.lab] = record
            created += 1

    # Process tasks
    for item in items:
        if item.type != "task":
            continue
        parent = lab_map.get(item.lab)
        if not parent:
            continue
        existing = (
            await session.exec(
                select(ItemRecord).where(
                    ItemRecord.title == item.title, ItemRecord.parent_id == parent.id
                )
            )
        ).first()
        if not existing:
            record = ItemRecord(type="task", title=item.title, parent_id=parent.id)
            session.add(record)
            created += 1

    await session.commit()
    return created


async def load_logs(
    logs: list[ApiLog],
    items_catalog: list[ApiItem],
    session: AsyncSession,
) -> int:
    """Load interaction logs into the database."""
    # Build lookup: (lab_short_id, task_short_id) → title
    title_lookup: dict[tuple[str, str | None], str] = {}
    for item in items_catalog:
        key = (item.lab, item.task)
        title_lookup[key] = item.title

    created = 0
    for log in logs:
        # Find or create learner
        learner = (
            await session.exec(
                select(Learner).where(Learner.external_id == log.student_id)
            )
        ).first()
        if not learner:
            learner = Learner(
                external_id=log.student_id,
                student_group=log.group,
            )
            session.add(learner)
            await session.flush()

        # Find item
        title = title_lookup.get((log.lab, log.task))
        if not title:
            continue
        item = (
            await session.exec(select(ItemRecord).where(ItemRecord.title == title))
        ).first()
        if not item:
            continue

        # Skip if already exists (idempotent upsert)
        existing = (
            await session.exec(
                select(InteractionLog).where(InteractionLog.external_id == log.id)
            )
        ).first()
        if existing:
            continue

        # Use API score if available; otherwise compute from passed/total
        score = log.score
        if score is None and log.passed is not None and log.total and log.total > 0:
            score = round((log.passed / log.total) * 100, 1)

        assert learner.id is not None
        assert item.id is not None
        interaction = InteractionLog(
            external_id=log.id,
            learner_id=learner.id,
            item_id=item.id,
            kind="attempt",
            score=score,
            checks_passed=log.passed,
            checks_total=log.total,
            created_at=datetime.fromisoformat(log.submitted_at),
        )
        session.add(interaction)
        created += 1

    await session.commit()
    return created


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


async def sync(session: AsyncSession) -> dict[str, int]:
    """Run the full ETL pipeline."""
    # Fetch and load items
    api_items = await fetch_items()
    await load_items(api_items, session)

    # Determine last sync point
    result = (await session.exec(select(func.max(InteractionLog.created_at)))).first()
    since = result if result else None

    # Fetch and load logs
    logs = await fetch_logs(since)
    new_count = await load_logs(logs, api_items, session)

    # Total count
    total = (await session.exec(select(func.count(col(InteractionLog.id))))).one()

    return {"new_records": new_count, "total_records": total}
