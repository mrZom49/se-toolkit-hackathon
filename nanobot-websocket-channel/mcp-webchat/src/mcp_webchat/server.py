"""Stdio MCP server exposing structured WebChat delivery tools."""

from __future__ import annotations

import json
import os
from collections.abc import Awaitable, Callable, Sequence
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool
from nanobot_channel_protocol.schemas import OutboundPayload
from pydantic import BaseModel, Field, TypeAdapter

from mcp_webchat.ui_relay import UIRelayClient

_ui_relay_url: str = ""
_ui_relay_token: str = ""
_outbound_adapter: TypeAdapter[OutboundPayload] = TypeAdapter(OutboundPayload)

server = Server("webchat")


class _UiMessageQuery(BaseModel):
    chat_id: str = Field(description="Active WebChat chat ID from the runtime context.")
    payload: dict[str, Any] = Field(
        description=(
            "Structured outbound payload with type text, choice, confirm, or composite."
        )
    )


def _ui_relay() -> UIRelayClient:
    if not _ui_relay_url:
        raise RuntimeError("UI relay URL not configured. Set NANOBOT_UI_RELAY_URL.")
    if not _ui_relay_token:
        raise RuntimeError("UI relay token not configured. Set NANOBOT_UI_RELAY_TOKEN.")
    return UIRelayClient(_ui_relay_url, _ui_relay_token)


def _text(data: BaseModel | Sequence[BaseModel] | dict[str, Any]) -> list[TextContent]:
    if isinstance(data, BaseModel):
        payload: object = data.model_dump()
    elif isinstance(data, dict):
        payload = data
    else:
        payload = [item.model_dump() for item in data]
    return [TextContent(type="text", text=json.dumps(payload, ensure_ascii=False))]


async def _ui_message(args: _UiMessageQuery) -> list[TextContent]:
    _outbound_adapter.validate_python(args.payload)
    result = await _ui_relay().send(chat_id=args.chat_id, payload=args.payload)
    return _text(result)


_Registry = tuple[type[BaseModel], Callable[..., Awaitable[list[TextContent]]], Tool]
_TOOLS: dict[str, _Registry] = {}


def _register(
    name: str,
    description: str,
    model: type[BaseModel],
    handler: Callable[..., Awaitable[list[TextContent]]],
) -> None:
    schema = model.model_json_schema()
    schema.pop("$defs", None)
    schema.pop("title", None)
    _TOOLS[name] = (
        model,
        handler,
        Tool(name=name, description=description, inputSchema=schema),
    )


_register(
    "ui_message",
    "Send a validated structured UI payload to an active WebChat client by chat ID.",
    _UiMessageQuery,
    _ui_message,
)


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [entry[2] for entry in _TOOLS.values()]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any] | None) -> list[TextContent]:
    entry = _TOOLS.get(name)
    if entry is None:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]

    model_cls, handler, _ = entry
    try:
        args = model_cls.model_validate(arguments or {})
        return await handler(args)
    except Exception as exc:
        return [TextContent(type="text", text=f"Error: {type(exc).__name__}: {exc}")]


async def main() -> None:
    global _ui_relay_url, _ui_relay_token
    _ui_relay_url = os.environ.get("NANOBOT_UI_RELAY_URL", "")
    _ui_relay_token = os.environ.get("NANOBOT_UI_RELAY_TOKEN", "")
    async with stdio_server() as (read_stream, write_stream):
        init_options = server.create_initialization_options()
        await server.run(read_stream, write_stream, init_options)
