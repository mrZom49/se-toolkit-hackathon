"""Stdio MCP server exposing observability tools (VictoriaLogs and VictoriaTraces)."""

from __future__ import annotations

import asyncio
import json
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent

from mcp_obs.client import ObservabilityClient
from mcp_obs.tools import TOOLS_BY_NAME


def _text(data: Any) -> list[TextContent]:
    if isinstance(data, dict):
        payload = data
    else:
        payload = data
    return [TextContent(type="text", text=json.dumps(payload, ensure_ascii=False))]


def create_server(client: ObservabilityClient) -> Server:
    server = Server("mcp-obs")

    @server.list_tools()
    async def list_tools() -> list:
        from mcp.types import Tool

        return [
            Tool(
                name=spec.name,
                description=spec.description,
                inputSchema=spec.input_schema,
            )
            for spec in TOOLS_BY_NAME.values()
        ]

    @server.call_tool()
    async def call_tool(
        name: str, arguments: dict[str, Any] | None
    ) -> list[TextContent]:
        spec = TOOLS_BY_NAME.get(name)
        if spec is None:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]
        try:
            if name == "mcp_obs_logs_search":
                from mcp_obs.tools import LogsSearchArgs

                args = LogsSearchArgs.model_validate(arguments or {})
                result = await spec.handler(client, args)
            elif name == "mcp_obs_logs_error_count":
                from mcp_obs.tools import LogsErrorCountArgs

                args = LogsErrorCountArgs.model_validate(arguments or {})
                result = await spec.handler(client, args)
            elif name == "mcp_obs_traces_list":
                from mcp_obs.tools import TracesListArgs

                args = TracesListArgs.model_validate(arguments or {})
                result = await spec.handler(client, args)
            elif name == "mcp_obs_traces_get":
                from mcp_obs.tools import TracesGetArgs

                args = TracesGetArgs.model_validate(arguments or {})
                result = await spec.handler(client, args)
            else:
                return [TextContent(type="text", text=f"Unknown tool: {name}")]
            return _text(result)
        except Exception as exc:
            return [
                TextContent(type="text", text=f"Error: {type(exc).__name__}: {exc}")
            ]

    _ = list_tools, call_tool
    return server


async def main() -> None:
    client = ObservabilityClient()
    server = create_server(client)
    async with stdio_server() as (read_stream, write_stream):
        init_options = server.create_initialization_options()
        await server.run(read_stream, write_stream, init_options)


if __name__ == "__main__":
    asyncio.run(main())
