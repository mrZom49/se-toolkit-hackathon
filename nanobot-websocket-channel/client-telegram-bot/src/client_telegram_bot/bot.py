#!/usr/bin/env python3
"""SE Toolkit Bot - Telegram bot for LMS interaction."""

from __future__ import annotations

import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from client_telegram_bot.handlers import (
    MessageHandlers,
    SessionHandlers,
    cmd_help,
    cmd_start,
)
from client_telegram_bot.logging_config import configure_logging, event_fields
from client_telegram_bot.services.nanobot_client import NanobotClient
from client_telegram_bot.settings import settings

log = logging.getLogger(__name__)


def main() -> None:
    configure_logging()
    user_keys: dict[int, str] = {}
    nanobot_client = NanobotClient(
        ws_url=settings.nanobot_ws_url,
        access_key=settings.nanobot_access_key,
    )
    session = SessionHandlers(user_keys)
    messages = MessageHandlers(nanobot_client, user_keys)

    dp = Dispatcher()
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_help, Command("help"))
    dp.message.register(session.cmd_login, Command("login"))
    dp.message.register(session.cmd_logout, Command("logout"))
    dp.message.register(messages.handle_message)
    dp.callback_query.register(messages.handle_callback)

    log.info(
        "telegram_bot_starting",
        extra=event_fields("telegram_bot_starting", ws_url=settings.nanobot_ws_url),
    )
    dp.run_polling(Bot(token=settings.bot_token))


if __name__ == "__main__":
    main()
