"""WebSocket client for the nanobot AI agent gateway."""

import asyncio
import json
import logging
from typing import Any
from urllib.parse import urlencode

import websockets
from websockets.exceptions import ConnectionClosedError, WebSocketException

from client_telegram_bot.logging_config import event_fields

log = logging.getLogger(__name__)


class NanobotClientError(Exception):
    """Base class for Telegram-facing nanobot client failures."""


class NanobotAccessKeyError(NanobotClientError):
    """Raised when the deployment access key is rejected."""


class NanobotTimeoutError(NanobotClientError):
    """Raised when nanobot does not produce any response in time."""


class NanobotTransportError(NanobotClientError):
    """Raised when the websocket transport fails unexpectedly."""


class NanobotClient:
    """Forwards messages to the nanobot agent over WebSocket."""

    initial_response_timeout_s = 60
    trailing_response_timeout_s = 15

    def __init__(self, ws_url: str, access_key: str):
        self.ws_url = ws_url
        self.access_key = access_key

    async def ask(self, message: str, api_key: str = "") -> dict[str, Any]:
        """Send a message and return the agent's structured response.

        The deployment access key is always sent so the channel accepts the
        connection. If *api_key* is provided it is forwarded as an extra query
        parameter for setups that still use per-user LMS credentials.

        Returns a dict with at least ``type`` and ``content`` fields.
        """
        url = self.ws_url
        query: dict[str, str] = {"access_key": self.access_key}
        if api_key:
            query["api_key"] = api_key
        if query:
            url = f"{self.ws_url}?{urlencode(query)}"
        log.info(
            "telegram_websocket_request",
            extra=event_fields(
                "telegram_websocket_request",
                ws_url=self.ws_url,
                has_user_api_key=bool(api_key),
                message_length=len(message),
            ),
        )
        try:
            async with websockets.connect(url, close_timeout=5) as ws:
                await ws.send(json.dumps({"content": message}))
                latest_response: dict[str, Any] | None = None
                frame_count = 0

                while True:
                    timeout_s = (
                        self.trailing_response_timeout_s
                        if latest_response is not None
                        else self.initial_response_timeout_s
                    )
                    try:
                        raw = await asyncio.wait_for(ws.recv(), timeout=timeout_s)
                    except TimeoutError:
                        if latest_response is None:
                            raise NanobotTimeoutError(
                                "The AI agent did not reply in time."
                            ) from None
                        break

                    frame_count += 1
                    data: dict[str, Any] = json.loads(raw)
                    log.info(
                        "telegram_websocket_response",
                        extra=event_fields(
                            "telegram_websocket_response",
                            response_type=data.get("type", "legacy_text"),
                            has_content=bool(data.get("content")),
                            frame_count=frame_count,
                        ),
                    )
                    latest_response = data

                final_response = latest_response
                assert final_response is not None, "nanobot returned no response frames"

                log.info(
                    "telegram_websocket_response_final",
                    extra=event_fields(
                        "telegram_websocket_response_final",
                        response_type=final_response.get("type", "legacy_text"),
                        has_content=bool(final_response.get("content")),
                        frame_count=frame_count,
                    ),
                )
                # Backwards compat: if no type field, wrap as text
                if "type" not in final_response:
                    return {
                        "type": "text",
                        "content": final_response.get("content", ""),
                        "format": "markdown",
                    }
                return final_response
        except json.JSONDecodeError:
            log.exception(
                "telegram_websocket_invalid_json",
                extra=event_fields(
                    "telegram_websocket_invalid_json",
                    ws_url=self.ws_url,
                ),
            )
            raise NanobotTransportError(
                "The AI agent returned an unreadable response."
            ) from None
        except ConnectionClosedError as exc:
            if exc.rcvd is not None and exc.rcvd.code == 4001:
                log.warning(
                    "telegram_websocket_access_key_rejected",
                    extra=event_fields(
                        "telegram_websocket_access_key_rejected",
                        ws_url=self.ws_url,
                    ),
                )
                raise NanobotAccessKeyError(
                    "The Telegram bot is using an invalid deployment access key."
                ) from None
            log.exception(
                "telegram_websocket_error",
                extra=event_fields(
                    "telegram_websocket_error",
                    ws_url=self.ws_url,
                ),
            )
            raise NanobotTransportError(
                "The connection to the AI agent closed unexpectedly."
            ) from None
        except (OSError, WebSocketException):
            log.exception(
                "telegram_websocket_error",
                extra=event_fields(
                    "telegram_websocket_error",
                    ws_url=self.ws_url,
                ),
            )
            raise NanobotTransportError(
                "The connection to the AI agent failed."
            ) from None
