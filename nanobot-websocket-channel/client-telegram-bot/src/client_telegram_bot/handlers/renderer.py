"""Render structured nanobot messages as Telegram responses."""

from typing import Any

from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nanobot_channel_protocol.schemas import (
    ChoiceMessage,
    ConfirmMessage,
    OutboundPayload,
    TextPart,
)
from pydantic import TypeAdapter

TELEGRAM_MAX_LENGTH = 4096
_outbound_adapter: TypeAdapter[OutboundPayload] = TypeAdapter(OutboundPayload)


def _split_text(text: str, limit: int = TELEGRAM_MAX_LENGTH) -> list[str]:
    """Split text into chunks that fit Telegram's message length limit."""
    if len(text) <= limit:
        return [text]
    chunks: list[str] = []
    while text:
        if len(text) <= limit:
            chunks.append(text)
            break
        # Try to split at last newline within limit
        cut = text.rfind("\n", 0, limit)
        if cut == -1:
            cut = limit
        chunks.append(text[:cut])
        text = text[cut:].lstrip("\n")
    return chunks


async def render(message: types.Message, response: dict[str, Any]) -> None:
    """Render a structured nanobot response to a Telegram chat."""
    parsed = _outbound_adapter.validate_python(response)

    if isinstance(parsed, TextPart):
        await _render_text(message, parsed)
    elif isinstance(parsed, ChoiceMessage):
        await _render_choice(message, parsed)
    elif isinstance(parsed, ConfirmMessage):
        await _render_confirm(message, parsed)
    else:
        for part in parsed.parts:
            await render(message, part.model_dump())


async def _render_text(message: types.Message, response: TextPart) -> None:
    for chunk in _split_text(response.content):
        await message.answer(chunk)


async def _render_choice(message: types.Message, response: ChoiceMessage) -> None:
    content = response.content or "Choose an option:"
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=opt.label, callback_data=opt.value)]
            for opt in response.options
        ]
    )
    await message.answer(content, reply_markup=keyboard)


async def _render_confirm(message: types.Message, response: ConfirmMessage) -> None:
    content = response.content or "Are you sure?"
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Yes", callback_data="yes"),
                InlineKeyboardButton(text="No", callback_data="no"),
            ]
        ]
    )
    await message.answer(content, reply_markup=keyboard)
