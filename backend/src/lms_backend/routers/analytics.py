"""Router for analytics endpoints.

Each endpoint performs SQL aggregation queries on the interaction data
populated by the ETL pipeline. All endpoints require a `lab` query
parameter to filter results by lab (e.g., "lab-01").
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy import case, cast, func, Numeric
from sqlmodel import col, select
from sqlmodel.ext.asyncio.session import AsyncSession

from lms_backend.database import get_session
from lms_backend.models.interaction import InteractionLog
from lms_backend.models.item import ItemRecord
from lms_backend.models.learner import Learner

router = APIRouter()


async def _find_lab_and_tasks(
    lab: str, session: AsyncSession
) -> tuple[ItemRecord | None, list[int | None]]:
    """Find a lab item and its child task IDs."""
    # Convert "lab-04" → "Lab 04" pattern for title matching
    lab_number = lab.replace("lab-", "").lstrip("0") or "0"
    lab_padded = lab.replace("lab-", "").zfill(2)

    # Search for lab by title
    labs = (
        await session.exec(select(ItemRecord).where(ItemRecord.type == "lab"))
    ).all()
    lab_item = None
    for item in labs:
        if f"Lab {lab_padded}" in item.title or f"Lab {lab_number}" in item.title:
            lab_item = item
            break

    if not lab_item:
        return None, []

    # Find child tasks
    tasks = (
        await session.exec(
            select(ItemRecord).where(ItemRecord.parent_id == lab_item.id)
        )
    ).all()

    item_ids = [lab_item.id] + [t.id for t in tasks]
    return lab_item, item_ids


@router.get("/scores")
async def get_scores(
    lab: str = Query(..., description="Lab identifier, e.g. 'lab-01'"),
    session: AsyncSession = Depends(get_session),
):
    """Score distribution histogram for a given lab."""
    _, item_ids = await _find_lab_and_tasks(lab, session)
    if not item_ids:
        return [
            {"bucket": "0-25", "count": 0},
            {"bucket": "26-50", "count": 0},
            {"bucket": "51-75", "count": 0},
            {"bucket": "76-100", "count": 0},
        ]

    bucket = case(
        (col(InteractionLog.score) <= 25, "0-25"),
        (col(InteractionLog.score) <= 50, "26-50"),
        (col(InteractionLog.score) <= 75, "51-75"),
        else_="76-100",
    )

    stmt = (
        select(bucket.label("bucket"), func.count().label("count"))
        .where(
            col(InteractionLog.item_id).in_(item_ids),
            col(InteractionLog.score).is_not(None),
        )
        .group_by(bucket)
    )

    rows = (await session.exec(stmt)).all()
    result_map = {bucket: count for bucket, count in rows}

    return [
        {"bucket": b, "count": result_map.get(b, 0)}
        for b in ["0-25", "26-50", "51-75", "76-100"]
    ]


@router.get("/pass-rates")
async def get_pass_rates(
    lab: str = Query(..., description="Lab identifier, e.g. 'lab-01'"),
    session: AsyncSession = Depends(get_session),
) -> list[dict[str, str | float | int]]:
    """Per-task pass rates for a given lab."""
    lab_item, _ = await _find_lab_and_tasks(lab, session)
    if not lab_item:
        return []

    tasks = (
        await session.exec(
            select(ItemRecord).where(ItemRecord.parent_id == lab_item.id)
        )
    ).all()

    results: list[dict[str, str | float | int]] = []
    for task in sorted(tasks, key=lambda t: t.title):
        stmt = select(
            func.round(cast(func.avg(InteractionLog.score), Numeric), 1).label(
                "avg_score"
            ),
            func.count().label("attempts"),
        ).where(
            InteractionLog.item_id == task.id,
            col(InteractionLog.score).is_not(None),
        )
        row = (await session.exec(stmt)).first()
        if row:
            avg_score, attempts = row
            if attempts > 0:
                results.append(
                    {
                        "task": task.title,
                        "avg_score": float(avg_score) if avg_score else 0.0,
                        "attempts": attempts,
                    }
                )

    return results


@router.get("/timeline")
async def get_timeline(
    lab: str = Query(..., description="Lab identifier, e.g. 'lab-01'"),
    session: AsyncSession = Depends(get_session),
) -> list[dict[str, str | int]]:
    """Submissions per day for a given lab."""
    _, item_ids = await _find_lab_and_tasks(lab, session)
    if not item_ids:
        return []

    stmt = (
        select(
            func.date(InteractionLog.created_at).label("date"),
            func.count().label("submissions"),
        )
        .where(col(InteractionLog.item_id).in_(item_ids))
        .group_by(func.date(InteractionLog.created_at))
        .order_by(func.date(InteractionLog.created_at))
    )

    rows = (await session.exec(stmt)).all()
    return [
        {"date": str(date), "submissions": submissions} for date, submissions in rows
    ]


@router.get("/groups")
async def get_groups(
    lab: str = Query(..., description="Lab identifier, e.g. 'lab-01'"),
    session: AsyncSession = Depends(get_session),
) -> list[dict[str, str | float | int]]:
    """Per-group performance for a given lab."""
    _, item_ids = await _find_lab_and_tasks(lab, session)
    if not item_ids:
        return []

    stmt = (
        select(
            col(Learner.student_group),
            func.round(cast(func.avg(InteractionLog.score), Numeric), 1).label(
                "avg_score"
            ),
            func.count(func.distinct(InteractionLog.learner_id)).label("students"),
        )
        .join(Learner, col(InteractionLog.learner_id) == col(Learner.id))
        .where(
            col(InteractionLog.item_id).in_(item_ids),
            col(InteractionLog.score).is_not(None),
        )
        .group_by(col(Learner.student_group))
        .order_by(col(Learner.student_group))
    )

    rows = (await session.exec(stmt)).all()
    return [
        {
            "group": group,
            "avg_score": float(avg_score) if avg_score else 0.0,
            "students": students,
        }
        for group, avg_score, students in rows
    ]


@router.get("/completion-rate")
async def get_completion_rate(
    lab: str = Query(..., description="Lab identifier, e.g. 'lab-01'"),
    session: AsyncSession = Depends(get_session),
):
    """Completion rate for a given lab — percentage of learners who scored >= 60."""
    _, item_ids = await _find_lab_and_tasks(lab, session)

    # Count distinct learners with any interaction
    total_stmt = select(func.count(func.distinct(InteractionLog.learner_id))).where(
        col(InteractionLog.item_id).in_(item_ids)
    )
    total_learners = (await session.exec(total_stmt)).one()

    # Count distinct learners who scored >= 60
    passed_stmt = select(func.count(func.distinct(InteractionLog.learner_id))).where(
        col(InteractionLog.item_id).in_(item_ids),
        col(InteractionLog.score) >= 60,
    )
    passed_learners = (await session.exec(passed_stmt)).one()

    rate = (passed_learners / total_learners) * 100 if total_learners else 0.0

    return {
        "lab": lab,
        "completion_rate": round(rate, 1),
        "passed": passed_learners,
        "total": total_learners,
    }


@router.get("/top-learners")
async def get_top_learners(
    lab: str = Query(..., description="Lab identifier, e.g. 'lab-01'"),
    limit: int = Query(default=10, description="Number of top learners to return"),
    session: AsyncSession = Depends(get_session),
) -> list[dict[str, int | float]]:
    """Top learners by average score for a given lab."""
    _, item_ids = await _find_lab_and_tasks(lab, session)
    if not item_ids:
        return []

    stmt = (
        select(
            InteractionLog.learner_id,
            func.avg(InteractionLog.score).label("avg_score"),
            func.count().label("attempts"),
        )
        .where(col(InteractionLog.item_id).in_(item_ids))
        .group_by(col(InteractionLog.learner_id))
    )

    rows = (await session.exec(stmt)).all()

    ranked = sorted(rows, key=lambda r: r[1], reverse=True)

    return [
        {
            "learner_id": learner_id,
            "avg_score": round(avg_score, 1),
            "attempts": attempts,
        }
        for learner_id, avg_score, attempts in ranked[:limit]
    ]
