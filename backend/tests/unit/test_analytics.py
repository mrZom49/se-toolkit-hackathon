"""Unit tests for analytics endpoints.

These tests use an in-memory SQLite database with pre-loaded fixture data.
Students implement the analytics endpoints to make these tests pass.
Run with: uv run poe test
"""

from collections.abc import AsyncGenerator

import pytest
from datetime import datetime
from httpx import ASGITransport, AsyncClient
from sqlalchemy import JSON, Table
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from lms_backend.models.item import ItemRecord
from lms_backend.models.learner import Learner
from lms_backend.models.interaction import InteractionLog


def _patch_jsonb_to_json() -> None:
    """Replace PostgreSQL JSONB columns with generic JSON for SQLite."""
    from sqlalchemy.dialects.postgresql import JSONB

    table: Table = SQLModel.metadata.tables["item"]
    for col in table.columns:
        if isinstance(col.type, JSONB):
            col.type = JSON()


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
async def engine() -> AsyncGenerator[AsyncEngine]:
    """Create an in-memory async SQLite engine with test schema."""
    _patch_jsonb_to_json()

    eng = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with eng.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield eng
    await eng.dispose()


@pytest.fixture
async def session(engine: AsyncEngine):
    """Provide a database session bound to the test engine."""
    async with AsyncSession(engine) as sess:
        yield sess


@pytest.fixture
async def seed_data(session: AsyncSession):
    """Populate the test database with realistic fixture data."""
    # Lab and tasks
    lab = ItemRecord(id=1, type="lab", title="Lab 04 — Testing", parent_id=None)
    task_setup = ItemRecord(id=2, type="task", title="Repository Setup", parent_id=1)
    task_tests = ItemRecord(id=3, type="task", title="Back-end Testing", parent_id=1)
    task_frontend = ItemRecord(id=4, type="task", title="Add Front-end", parent_id=1)
    session.add_all([lab, task_setup, task_tests, task_frontend])

    # Another lab (should not appear in lab-04 queries)
    other_lab = ItemRecord(id=5, type="lab", title="Lab 03 — Backend", parent_id=None)
    session.add(other_lab)

    # Learners from different groups
    learners = [
        Learner(id=1, external_id="stu001", student_group="B23-CS-01"),
        Learner(id=2, external_id="stu002", student_group="B23-CS-01"),
        Learner(id=3, external_id="stu003", student_group="B23-CS-02"),
        Learner(id=4, external_id="stu004", student_group="B23-CS-02"),
        Learner(id=5, external_id="stu005", student_group="B23-DS-01"),
    ]
    session.add_all(learners)

    # Interactions with scores
    interactions = [
        # task_setup: high scores
        InteractionLog(
            id=1,
            external_id=101,
            learner_id=1,
            item_id=2,
            kind="attempt",
            score=100.0,
            checks_passed=4,
            checks_total=4,
            created_at=datetime(2026, 2, 28, 10, 0),
        ),
        InteractionLog(
            id=2,
            external_id=102,
            learner_id=2,
            item_id=2,
            kind="attempt",
            score=75.0,
            checks_passed=3,
            checks_total=4,
            created_at=datetime(2026, 2, 28, 11, 0),
        ),
        InteractionLog(
            id=3,
            external_id=103,
            learner_id=3,
            item_id=2,
            kind="attempt",
            score=100.0,
            checks_passed=4,
            checks_total=4,
            created_at=datetime(2026, 2, 28, 14, 0),
        ),
        InteractionLog(
            id=4,
            external_id=104,
            learner_id=4,
            item_id=2,
            kind="attempt",
            score=50.0,
            checks_passed=2,
            checks_total=4,
            created_at=datetime(2026, 3, 1, 9, 0),
        ),
        # task_tests: mixed scores
        InteractionLog(
            id=5,
            external_id=105,
            learner_id=1,
            item_id=3,
            kind="attempt",
            score=80.0,
            checks_passed=4,
            checks_total=5,
            created_at=datetime(2026, 3, 1, 10, 0),
        ),
        InteractionLog(
            id=6,
            external_id=106,
            learner_id=2,
            item_id=3,
            kind="attempt",
            score=20.0,
            checks_passed=1,
            checks_total=5,
            created_at=datetime(2026, 3, 1, 11, 0),
        ),
        InteractionLog(
            id=7,
            external_id=107,
            learner_id=5,
            item_id=3,
            kind="attempt",
            score=60.0,
            checks_passed=3,
            checks_total=5,
            created_at=datetime(2026, 3, 2, 10, 0),
        ),
        # task_frontend: low scores
        InteractionLog(
            id=8,
            external_id=108,
            learner_id=3,
            item_id=4,
            kind="attempt",
            score=0.0,
            checks_passed=0,
            checks_total=3,
            created_at=datetime(2026, 3, 2, 15, 0),
        ),
        # other lab interaction (should be excluded)
        InteractionLog(
            id=9,
            external_id=109,
            learner_id=1,
            item_id=5,
            kind="attempt",
            score=100.0,
            checks_passed=5,
            checks_total=5,
            created_at=datetime(2026, 3, 2, 16, 0),
        ),
    ]
    session.add_all(interactions)
    await session.commit()


@pytest.fixture
async def client(engine: AsyncEngine, seed_data: None):
    """Create a test HTTP client with the test database injected."""
    from lms_backend.main import app
    from lms_backend.database import get_session

    async def override_session():
        async with AsyncSession(engine) as sess:
            yield sess

    app.dependency_overrides[get_session] = override_session

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c

    app.dependency_overrides.clear()


# ---------------------------------------------------------------------------
# Tests: GET /analytics/scores
# ---------------------------------------------------------------------------


class TestScores:
    @pytest.mark.asyncio
    async def test_scores_returns_200(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/scores",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_scores_returns_four_buckets(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/scores",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        data = resp.json()
        assert len(data) == 4
        buckets = {d["bucket"] for d in data}
        assert buckets == {"0-25", "26-50", "51-75", "76-100"}

    @pytest.mark.asyncio
    async def test_scores_counts_are_correct(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/scores",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        data = {d["bucket"]: d["count"] for d in resp.json()}
        # 0-25: scores 0, 20 → 2
        # 26-50: score 50 → 1
        # 51-75: scores 60, 75 → 2
        # 76-100: scores 80, 100, 100 → 3
        assert data["0-25"] == 2
        assert data["26-50"] == 1
        assert data["51-75"] == 2
        assert data["76-100"] == 3

    @pytest.mark.asyncio
    async def test_scores_excludes_other_labs(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/scores",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        total = sum(d["count"] for d in resp.json())
        assert total == 8  # 9 interactions total, but 1 belongs to lab-03


# ---------------------------------------------------------------------------
# Tests: GET /analytics/pass-rates
# ---------------------------------------------------------------------------


class TestPassRates:
    @pytest.mark.asyncio
    async def test_pass_rates_returns_200(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/pass-rates",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_pass_rates_returns_tasks(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/pass-rates",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        data = resp.json()
        tasks = {d["task"] for d in data}
        assert "Repository Setup" in tasks
        assert "Back-end Testing" in tasks
        assert "Add Front-end" in tasks

    @pytest.mark.asyncio
    async def test_pass_rates_avg_scores(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/pass-rates",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        data = {d["task"]: d for d in resp.json()}
        # Repository Setup: (100 + 75 + 100 + 50) / 4 = 81.25 → 81.2
        assert data["Repository Setup"]["avg_score"] == pytest.approx(  # pyright: ignore[reportUnknownMemberType]
            81.2, abs=0.1
        )
        assert data["Repository Setup"]["attempts"] == 4
        # Back-end Testing: (80 + 20 + 60) / 3 = 53.33 → 53.3
        assert data["Back-end Testing"]["avg_score"] == pytest.approx(  # pyright: ignore[reportUnknownMemberType]
            53.3, abs=0.1
        )
        assert data["Back-end Testing"]["attempts"] == 3

    @pytest.mark.asyncio
    async def test_pass_rates_has_correct_fields(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/pass-rates",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        for item in resp.json():
            assert "task" in item
            assert "avg_score" in item
            assert "attempts" in item


# ---------------------------------------------------------------------------
# Tests: GET /analytics/timeline
# ---------------------------------------------------------------------------


class TestTimeline:
    @pytest.mark.asyncio
    async def test_timeline_returns_200(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/timeline",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_timeline_has_correct_dates(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/timeline",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        data = resp.json()
        dates = {d["date"] for d in data}
        assert "2026-02-28" in dates
        assert "2026-03-01" in dates
        assert "2026-03-02" in dates

    @pytest.mark.asyncio
    async def test_timeline_submission_counts(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/timeline",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        data = {d["date"]: d["submissions"] for d in resp.json()}
        # Feb 28: interactions 1, 2, 3 → 3
        assert data["2026-02-28"] == 3
        # Mar 1: interactions 4, 5, 6 → 3
        assert data["2026-03-01"] == 3
        # Mar 2: interactions 7, 8 → 2
        assert data["2026-03-02"] == 2

    @pytest.mark.asyncio
    async def test_timeline_ordered_by_date(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/timeline",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        dates = [d["date"] for d in resp.json()]
        assert dates == sorted(dates)


# ---------------------------------------------------------------------------
# Tests: GET /analytics/groups
# ---------------------------------------------------------------------------


class TestGroups:
    @pytest.mark.asyncio
    async def test_groups_returns_200(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/groups",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_groups_has_all_groups(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/groups",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        data = resp.json()
        groups = {d["group"] for d in data}
        assert "B23-CS-01" in groups
        assert "B23-CS-02" in groups
        assert "B23-DS-01" in groups

    @pytest.mark.asyncio
    async def test_groups_student_counts(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/groups",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        data = {d["group"]: d for d in resp.json()}
        # B23-CS-01: learners 1, 2 → 2 students
        assert data["B23-CS-01"]["students"] == 2
        # B23-CS-02: learners 3, 4 → 2 students
        assert data["B23-CS-02"]["students"] == 2
        # B23-DS-01: learner 5 → 1 student
        assert data["B23-DS-01"]["students"] == 1

    @pytest.mark.asyncio
    async def test_groups_avg_scores(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/groups",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        data = {d["group"]: d for d in resp.json()}
        # B23-CS-01: scores 100, 75, 80, 20 → avg 68.75 → 68.8
        assert data["B23-CS-01"]["avg_score"] == pytest.approx(  # pyright: ignore[reportUnknownMemberType]
            68.8, abs=0.1
        )
        # B23-CS-02: scores 100, 50, 0 → avg 50.0
        assert data["B23-CS-02"]["avg_score"] == pytest.approx(  # pyright: ignore[reportUnknownMemberType]
            50.0, abs=0.1
        )
        # B23-DS-01: score 60 → avg 60.0
        assert data["B23-DS-01"]["avg_score"] == pytest.approx(  # pyright: ignore[reportUnknownMemberType]
            60.0, abs=0.1
        )

    @pytest.mark.asyncio
    async def test_groups_has_correct_fields(self, client: AsyncClient):
        resp = await client.get(
            "/analytics/groups",
            params={"lab": "lab-04"},
            headers={"Authorization": "Bearer test"},
        )
        for item in resp.json():
            assert "group" in item
            assert "avg_score" in item
            assert "students" in item
