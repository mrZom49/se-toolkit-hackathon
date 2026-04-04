"""Pydantic models for interactions."""

from datetime import datetime, timezone

from sqlmodel import Field, SQLModel

# Ensure referenced FK target tables are registered in SQLModel metadata
# whenever InteractionLog is imported.


class InteractionLog(SQLModel, table=True):
    """An interaction log entry in the database."""

    __tablename__ = "interacts"

    id: int | None = Field(default=None, primary_key=True)
    external_id: int | None = Field(default=None, unique=True)
    learner_id: int = Field(foreign_key="learner.id")
    item_id: int = Field(foreign_key="item.id")
    kind: str
    score: float | None = None
    checks_passed: int | None = None
    checks_total: int | None = None
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )


class InteractionLogCreate(SQLModel):
    """Request schema for creating an interaction log."""

    learner_id: int
    item_id: int
    kind: str

    model_config = {
        "json_schema_extra": {
            "example": """{
                "learner_id": 1,
                "item_id": 1,
                "kind": "attempt"
            }"""
        }
    }


class InteractionModel(SQLModel):
    """Response schema for an interaction."""

    id: int
    learner_id: int
    item_id: int
    kind: str
    created_at: datetime
