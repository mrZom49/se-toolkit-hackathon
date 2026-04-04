"""WebChat channel — WebSocket server for web clients."""

from __future__ import annotations

import asyncio
import json
import logging
import os
import uuid
from typing import Any
from urllib.parse import parse_qs, urlparse

from aiohttp import web
from nanobot_channel_protocol.schemas import OutboundPayload
from pydantic import Field, TypeAdapter, ValidationError
import websockets
from websockets.asyncio.server import Server as WebSocketServer
from websockets.asyncio.server import ServerConnection

from nanobot.bus.events import OutboundMessage
from nanobot.bus.queue import MessageBus
from nanobot.channels.base import BaseChannel
from nanobot.config.schema import Base

from .structured import parse_outbound

logger = logging.getLogger(__name__)
_OUTBOUND_ADAPTER: TypeAdapter[OutboundPayload] = TypeAdapter(OutboundPayload)


class WebChatConfig(Base):
    """WebChat channel configuration."""

    enabled: bool = False
    host: str = "0.0.0.0"
    port: int = 8765
    allow_from: list[str] = Field(default_factory=lambda: ["*"])
    relay_host: str = "127.0.0.1"
    relay_port: int = 8766


class WebChatChannel(BaseChannel):
    """WebSocket-based web chat channel.

    Each WebSocket connection is treated as an independent chat session.
    Protocol (JSON):
        Client -> Server:  {"content": "hello"}
        Server -> Client:  {"content": "response text"}

    Access control:
        Set NANOBOT_ACCESS_KEY env var to require authentication.
        Clients pass the key via query parameter: ws://host:port?access_key=SECRET
        Connections without a valid key are rejected. LMS-aware clients may
        also provide ?api_key=...; when present it is forwarded to the agent
        as a prompt prefix for backwards compatibility.
    """

    name = "webchat"
    display_name = "WebChat"

    @classmethod
    def default_config(cls) -> dict[str, Any]:
        return WebChatConfig().model_dump(by_alias=True)

    def __init__(self, config: Any, bus: MessageBus):
        if isinstance(config, dict):
            config = WebChatConfig.model_validate(config)
        super().__init__(config, bus)
        self.config: WebChatConfig = config
        self._connections: dict[str, ServerConnection] = {}
        self._server: WebSocketServer | None = None
        self._access_key: str = os.environ.get("NANOBOT_ACCESS_KEY", "")
        self._relay_host: str = os.environ.get(
            "NANOBOT_UI_RELAY_HOST", self.config.relay_host
        )
        self._relay_port: int = int(
            os.environ.get("NANOBOT_UI_RELAY_PORT", str(self.config.relay_port))
        )
        self._relay_token: str = os.environ.get(
            "NANOBOT_UI_RELAY_TOKEN", self._access_key
        )
        self._relay_runner: web.AppRunner | None = None
        self._relay_site: web.TCPSite | None = None

    async def start(self) -> None:
        """Start the WebSocket server."""
        self._running = True
        if not self._access_key:
            raise RuntimeError("WebChat: NANOBOT_ACCESS_KEY must be set")
        await self._start_relay()
        logger.info("WebChat starting on %s:%s", self.config.host, self.config.port)
        self._server = await websockets.serve(
            self._handle_ws,
            self.config.host,
            self.config.port,
        )
        while self._running:
            await asyncio.sleep(1)

    async def stop(self) -> None:
        """Stop the WebSocket server."""
        self._running = False
        if self._server:
            self._server.close()
            await self._server.wait_closed()
            self._server = None
        await self._stop_relay()
        self._connections.clear()

    async def send(self, msg: OutboundMessage) -> None:
        """Send a message back to the client via its WebSocket."""
        ws = self._connections.get(msg.chat_id)
        if ws is None:
            logger.warning("WebChat: no connection for chat_id=%s", msg.chat_id)
            return
        try:
            result = parse_outbound(msg.content)
            await ws.send(result.model_dump_json())
        except websockets.ConnectionClosed:
            logger.info("WebChat: connection closed for chat_id=%s", msg.chat_id)
            self._connections.pop(msg.chat_id, None)

    async def _handle_ws(self, ws: ServerConnection) -> None:
        """Handle a single WebSocket connection lifecycle."""
        # Validate access key
        path: str = ws.request.path if ws.request is not None else ""
        qs = parse_qs(urlparse(path).query)
        client_key: str = qs.get("access_key", [""])[0]
        api_key: str = qs.get("api_key", [""])[0].strip()

        if self._access_key and client_key != self._access_key:
            logger.warning("WebChat: rejected connection — invalid access key")
            await ws.close(4001, "Invalid access key")
            return

        chat_id = str(uuid.uuid4())
        self._connections[chat_id] = ws
        sender_id = chat_id

        logger.info("WebChat: new connection chat_id=%s", chat_id)

        try:
            async for raw in ws:
                try:
                    data = json.loads(raw)
                    content = data.get("content", "").strip()
                except (json.JSONDecodeError, AttributeError):
                    content = str(raw).strip()

                if not content:
                    continue

                if api_key:
                    # Preserve the legacy per-user LMS credential flow used by
                    # the Telegram client without reusing it as deployment auth.
                    content = f"[LMS_API_KEY={api_key}] {content}"

                await self._handle_message(
                    sender_id=sender_id,
                    chat_id=chat_id,
                    content=content,
                )
        except websockets.ConnectionClosed:
            pass
        finally:
            self._connections.pop(chat_id, None)
            logger.info("WebChat: disconnected chat_id=%s", chat_id)

    async def _start_relay(self) -> None:
        app = web.Application()
        app.router.add_post("/ui-message", self._handle_ui_message)
        self._relay_runner = web.AppRunner(app)
        await self._relay_runner.setup()
        self._relay_site = web.TCPSite(
            self._relay_runner, self._relay_host, self._relay_port
        )
        await self._relay_site.start()
        logger.info(
            "WebChat relay listening on %s:%s", self._relay_host, self._relay_port
        )

    async def _stop_relay(self) -> None:
        if self._relay_site is not None:
            await self._relay_site.stop()
            self._relay_site = None
        if self._relay_runner is not None:
            await self._relay_runner.cleanup()
            self._relay_runner = None

    async def _handle_ui_message(self, request: web.Request) -> web.Response:
        auth_header = request.headers.get("Authorization", "")
        expected = f"Bearer {self._relay_token}"
        if self._relay_token and auth_header != expected:
            raise web.HTTPUnauthorized(text="Invalid relay token")

        try:
            body = await request.json()
        except json.JSONDecodeError as exc:
            raise web.HTTPBadRequest(text=f"Invalid JSON body: {exc}") from exc

        chat_id = str(body.get("chat_id", "")).strip()
        if not chat_id:
            raise web.HTTPBadRequest(text="chat_id is required")

        try:
            payload = _OUTBOUND_ADAPTER.validate_python(body.get("payload"))
        except ValidationError as exc:
            raise web.HTTPBadRequest(text=f"Invalid outbound payload: {exc}") from exc

        ws = self._connections.get(chat_id)
        if ws is None:
            raise web.HTTPNotFound(text=f"No active connection for chat_id={chat_id}")

        try:
            await ws.send(payload.model_dump_json())
        except websockets.ConnectionClosed as exc:
            self._connections.pop(chat_id, None)
            raise web.HTTPGone(text=f"Connection closed for chat_id={chat_id}") from exc

        return web.json_response({"status": "sent", "chat_id": chat_id})
