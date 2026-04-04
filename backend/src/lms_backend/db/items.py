"""Database operations for items."""

import logging

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from lms_backend.models.item import ItemRecord

logger = logging.getLogger(__name__)


async def read_items(session: AsyncSession) -> list[ItemRecord]:
    """Read all items from the database."""
    try:
        logger.info(
            "db_query",
            extra={"event": "db_query", "table": "item", "operation": "select"},
        )
        result = await session.exec(select(ItemRecord))
        return list(result.all())
    except Exception as exc:
        logger.error(
            "db_query",
            extra={
                "event": "db_query",
                "table": "item",
                "operation": "select",
                "error": str(exc),
            },
        )
        raise


async def read_item(session: AsyncSession, item_id: int) -> ItemRecord | None:
    """Read a single item by id."""
    return await session.get(ItemRecord, item_id)


async def create_item(
    session: AsyncSession,
    type: str,
    parent_id: int | None,
    title: str,
    description: str,
) -> ItemRecord:
    """Create a new item in the database."""
    item = ItemRecord(
        type=type, parent_id=parent_id, title=title, description=description
    )
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


async def update_item(
    session: AsyncSession, item_id: int, title: str, description: str
) -> ItemRecord | None:
    """Update an existing item in the database."""
    item = await session.get(ItemRecord, item_id)
    if item is None:
        return None
    item.title = title
    item.description = description
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item
