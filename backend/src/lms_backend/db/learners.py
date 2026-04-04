"""Database operations for learners."""

from datetime import datetime

from sqlmodel import col, select
from sqlmodel.ext.asyncio.session import AsyncSession

from lms_backend.models.learner import Learner


async def read_learners(
    session: AsyncSession, enrolled_after: datetime | None = None
) -> list[Learner]:
    """Read all learners from the database, optionally filtered by enrollment date."""
    statement = select(Learner)
    if enrolled_after is not None:
        statement = statement.where(col(Learner.enrolled_at) >= enrolled_after)
    result = await session.exec(statement)
    return list(result.all())


async def create_learner(
    session: AsyncSession, external_id: str, student_group: str = ""
) -> Learner:
    """Create a new learner in the database."""
    learner = Learner(
        external_id=external_id, student_group=student_group, enrolled_at=datetime.now()
    )
    session.add(learner)
    await session.commit()
    await session.refresh(learner)
    return learner
