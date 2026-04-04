"""Route free-text messages to the nanobot AI agent via WebSocket."""

from __future__ import annotations

import logging
from typing import Any

from client_telegram_bot.services.nanobot_client import (
    NanobotAccessKeyError,
    NanobotClient,
    NanobotTimeoutError,
    NanobotTransportError,
)

log = logging.getLogger(__name__)


async def route_intent(
    user_message: str, nanobot_client: NanobotClient, api_key: str = ""
) -> dict[str, Any]:
    """Forward a natural language message to the nanobot agent.

    Returns a structured message dict (see nanobot/plan.md protocol spec).
    """
    try:
        return await nanobot_client.ask(user_message, api_key=api_key)
    except NanobotTimeoutError as exc:
        log.info("telegram_intent_timeout")
        return {
            "type": "text",
            "content": (
                "⏳ The AI agent is taking too long to answer.\n\n"
                f"{exc}\nPlease try again in a moment."
            ),
            "format": "markdown",
        }
    except NanobotAccessKeyError as exc:
        log.warning("telegram_intent_access_key_error")
        return {
            "type": "text",
            "content": (
                "🔒 The Telegram bot could not authenticate to the deployed "
                f"AI agent.\n\n{exc}"
            ),
            "format": "markdown",
        }
    except NanobotTransportError as exc:
        log.warning("telegram_intent_transport_error")
        return {
            "type": "text",
            "content": (
                "⚠️ The AI agent could not finish the reply because the "
                f"connection failed.\n\n{exc}"
            ),
            "format": "markdown",
        }
    except Exception as e:
        log.exception("telegram_intent_unexpected_error")
        return {
            "type": "text",
            "content": (
                "⚠️ Something unexpected went wrong while talking to the AI "
                f"agent.\n\n{e}"
            ),
            "format": "markdown",
        }
