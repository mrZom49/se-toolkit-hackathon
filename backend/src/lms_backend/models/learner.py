"""Pydantic models for learners."""

from datetime import datetime

from sqlmodel import Field, SQLModel


class Learner(SQLModel, table=True):
    """A learner in the learning management system."""

    __tablename__ = "learner"

    id: int | None = Field(default=None, primary_key=True)
    external_id: str = Field(unique=True)
    student_group: str = ""
    enrolled_at: datetime | None = Field(default=None)


class LearnerCreate(SQLModel):
    """Schema for creating a learner."""

    external_id: str
    student_group: str = ""
