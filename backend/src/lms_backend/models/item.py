"""Models for course items."""

from datetime import datetime, timezone
from typing import Any

from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Column, Field, SQLModel


# ===
# Database models
# ===
#
# These [`SQLModel`](https://sqlmodel.tiangolo.com/) classes map to the `item`
# PostgreSQL table. `SQLModel` combines SQLAlchemy (database ORM) with
# Pydantic (data validation) in a single class hierarchy.
#
# Items form a tree: course → labs → tasks → steps.
# The tree structure is stored using the
# [adjacency list](https://en.wikipedia.org/wiki/Adjacency_list) pattern (`parent_id`).
# Type-specific attributes are stored in a
# [`JSONB`](https://www.postgresql.org/docs/current/datatype-json.html) column.


class ItemRecord(SQLModel, table=True):
    """A row in the items table."""

    __tablename__ = "item"

    id: int | None = Field(default=None, primary_key=True)
    type: str = "step"
    parent_id: int | None = Field(default=None, foreign_key="item.id")
    title: str
    description: str = ""
    attributes: dict[str, Any] = Field(
        default_factory=dict, sa_column=Column(JSONB, nullable=False)
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )


class ItemCreate(SQLModel):
    """Schema for creating an item."""

    type: str = "step"
    parent_id: int | None = None
    title: str
    description: str = ""


class ItemUpdate(SQLModel):
    """Schema for updating an item."""

    title: str
    description: str = ""
