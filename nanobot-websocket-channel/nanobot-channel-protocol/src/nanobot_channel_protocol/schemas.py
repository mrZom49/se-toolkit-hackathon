"""Pydantic schemas for structured nanobot channel messages."""

from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, Discriminator, Field, Tag


class ChoiceOption(BaseModel):
    label: str
    value: str


class ChoiceMessage(BaseModel):
    type: Literal["choice"] = "choice"
    content: str = ""
    options: list[ChoiceOption] = Field(min_length=1)


class ConfirmMessage(BaseModel):
    type: Literal["confirm"] = "confirm"
    content: str


class TextPart(BaseModel):
    type: Literal["text"] = "text"
    content: str
    format: str = "markdown"


CompositePartMessage = ChoiceMessage | ConfirmMessage | TextPart


class CompositeMessage(BaseModel):
    type: Literal["composite"] = "composite"
    parts: list[CompositePartMessage] = Field(min_length=1)


StructuredMessage = Annotated[
    Annotated[ChoiceMessage, Tag("choice")]
    | Annotated[ConfirmMessage, Tag("confirm")]
    | Annotated[CompositeMessage, Tag("composite")],
    Discriminator("type"),
]

OutboundPayload = StructuredMessage | TextPart
