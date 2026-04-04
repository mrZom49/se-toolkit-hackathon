"""Database operations for interactions."""

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from lms_backend.models.interaction import InteractionLog


async def read_interactions(session: AsyncSession) -> list[InteractionLog]:
    """Read all interactions from the database."""
    result = await session.exec(select(InteractionLog))
    return list(result.all())


async def create_interaction(
    session: AsyncSession,
    learner_id: int,
    item_id: int,
    kind: str,
) -> InteractionLog:
    """Create a new interaction log in the database."""
    interaction = InteractionLog(learner_id=learner_id, item_id=item_id, kind=kind)
    session.add(interaction)
    await session.commit()
    await session.refresh(interaction)
    return interaction
