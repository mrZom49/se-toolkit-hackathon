"""Message and callback handlers for the Telegram bot."""

from __future__ import annotations

import logging

from aiogram import types

from client_telegram_bot.handlers.intent_router import route_intent
from client_telegram_bot.handlers.renderer import render
from client_telegram_bot.logging_config import event_fields
from client_telegram_bot.services.nanobot_client import NanobotClient

log = logging.getLogger(__name__)


class MessageHandlers:
    def __init__(
        self, nanobot_client: NanobotClient, user_keys: dict[int, str]
    ) -> None:
        self.nanobot_client = nanobot_client
        self.user_keys = user_keys

    async def handle_message(self, message: types.Message) -> None:
        if not message.from_user or not message.text:
            return
        api_key = self.user_keys.get(message.from_user.id, "")
        if not api_key:
            await message.answer("🔑 Please set your API key first: /login <api_key>")
            return
        log.info(
            "telegram_message",
            extra=event_fields(
                "telegram_message",
                user_id=message.from_user.id,
                chat_id=message.chat.id,
                message_length=len(message.text),
            ),
        )
        response = await route_intent(
            message.text, self.nanobot_client, api_key=api_key
        )
        await render(message, response)

    async def handle_callback(self, callback: types.CallbackQuery) -> None:
        await callback.answer()
        if not callback.from_user or not callback.data:
            return
        if not isinstance(callback.message, types.Message):
            return
        api_key = self.user_keys.get(callback.from_user.id, "")
        if not api_key:
            await callback.message.answer(
                "🔑 Please set your API key first: /login <api_key>"
            )
            return
        log.info(
            "telegram_callback",
            extra=event_fields(
                "telegram_callback",
                user_id=callback.from_user.id,
                chat_id=callback.message.chat.id,
                callback_data=callback.data,
            ),
        )
        response = await route_intent(
            callback.data, self.nanobot_client, api_key=api_key
        )
        await render(callback.message, response)
