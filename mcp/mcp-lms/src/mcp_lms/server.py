"""Stdio MCP server exposing LMS backend operations as typed tools."""

from __future__ import annotations

import asyncio
import json
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool
from pydantic import BaseModel

from mcp_lms.client import LMSClient
from mcp_lms.settings import resolve_settings
from mcp_lms.tools import TOOL_SPECS, TOOLS_BY_NAME, ToolPayload


def _text(data: ToolPayload) -> list[TextContent]:
    if isinstance(data, BaseModel):
        payload = data.model_dump()
    else:
        payload = [item.model_dump() for item in data]
    return [TextContent(type="text", text=json.dumps(payload, ensure_ascii=False))]


def create_server(client: LMSClient) -> Server:
    server = Server("lms")

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return [spec.as_tool() for spec in TOOL_SPECS]

    @server.call_tool()
    async def call_tool(
        name: str, arguments: dict[str, Any] | None
    ) -> list[TextContent]:
        spec = TOOLS_BY_NAME.get(name)
        if spec is None:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]
        try:
            args = spec.model.model_validate(arguments or {})
            return _text(await spec.handler(client, args))
        except Exception as exc:
            return [
                TextContent(type="text", text=f"Error: {type(exc).__name__}: {exc}")
            ]

    _ = list_tools, call_tool
    return server


async def main(base_url: str | None = None) -> None:
    settings = resolve_settings(base_url)
    async with LMSClient(settings.base_url, settings.api_key) as client:
        server = create_server(client)
        async with stdio_server() as (read_stream, write_stream):
            init_options = server.create_initialization_options()
            await server.run(read_stream, write_stream, init_options)


if __name__ == "__main__":
    asyncio.run(main())
