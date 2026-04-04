"""Session-oriented command handlers for the Telegram bot."""

from __future__ import annotations

import logging

from aiogram import types

from client_telegram_bot.logging_config import event_fields

log = logging.getLogger(__name__)


class SessionHandlers:
    def __init__(self, user_keys: dict[int, str]) -> None:
        self.user_keys = user_keys

    async def cmd_login(self, message: types.Message) -> None:
        if not message.from_user:
            return
        args = message.text.split()[1:] if message.text else []
        if not args:
            await message.answer("Usage: /login <api_key>")
            return
        self.user_keys[message.from_user.id] = args[0]
        log.info(
            "telegram_login",
            extra=event_fields("telegram_login", user_id=message.from_user.id),
        )
        await message.answer("✅ API key saved. You can now ask questions.")

    async def cmd_logout(self, message: types.Message) -> None:
        if not message.from_user:
            return
        self.user_keys.pop(message.from_user.id, None)
        log.info(
            "telegram_logout",
            extra=event_fields("telegram_logout", user_id=message.from_user.id),
        )
        await message.answer("🔓 API key removed.")
