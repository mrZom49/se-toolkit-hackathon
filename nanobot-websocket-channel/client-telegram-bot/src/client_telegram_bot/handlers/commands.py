"""Basic command handlers for the Telegram bot."""

from __future__ import annotations

import logging

from aiogram import types

from client_telegram_bot.logging_config import event_fields

log = logging.getLogger(__name__)


HELP_TEXT = (
    "📚 Available commands:\n\n"
    "• /start - Welcome message\n"
    "• /help - Show this help message\n"
    "• /login <api_key> - Set your LMS API key\n"
    "• /logout - Remove your LMS API key\n\n"
    "You can also ask questions in plain language, like:\n"
    "• 'Is the backend healthy?'\n"
    "• 'What labs are available?'\n"
    "• 'Show me the scores for lab-04'"
)

WELCOME_TEXT = (
    "👋 Welcome to SE Toolkit Bot!\n\n"
    "I'm your LMS assistant. To get started, set your API key:\n"
    "  /login <your-api-key>\n\n"
    "Then ask me anything in plain language,\n"
    "or type /help to see available commands."
)


async def cmd_start(message: types.Message) -> None:
    log.info(
        "telegram_start",
        extra=event_fields(
            "telegram_start",
            user_id=message.from_user.id if message.from_user else None,
        ),
    )
    await message.answer(WELCOME_TEXT)


async def cmd_help(message: types.Message) -> None:
    log.info(
        "telegram_help",
        extra=event_fields(
            "telegram_help",
            user_id=message.from_user.id if message.from_user else None,
        ),
    )
    await message.answer(HELP_TEXT)
