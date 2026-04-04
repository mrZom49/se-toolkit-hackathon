"""Tool specifications for observability MCP tools."""

import json
import logging
from typing import Any, Callable, Coroutine

from pydantic import BaseModel

from mcp_obs.client import ObservabilityClient

logger = logging.getLogger(__name__)


class LogsSearchArgs(BaseModel):
    query: str
    limit: int = 10


class LogsErrorCountArgs(BaseModel):
    service: str | None = None
    time_window: str = "1h"


class TracesListArgs(BaseModel):
    service: str
    limit: int = 10


class TracesGetArgs(BaseModel):
    trace_id: str


async def logs_search_handler(
    client: ObservabilityClient, args: LogsSearchArgs
) -> list[dict[str, Any]]:
    """Search logs in VictoriaLogs."""
    results = await client.logs_search(args.query, args.limit)
    parsed = []
    for item in results:
        if isinstance(item, dict):
            parsed.append(item)
        elif isinstance(item, str):
            try:
                parsed.append(json.loads(item))
            except json.JSONDecodeError:
                parsed.append({"raw": item})
        else:
            parsed.append({"raw": str(item)})
    return parsed


async def logs_error_count_handler(
    client: ObservabilityClient, args: LogsErrorCountArgs
) -> dict[str, int]:
    """Count errors per service over a time window."""
    return await client.logs_error_count(args.service, args.time_window)


async def traces_list_handler(
    client: ObservabilityClient, args: TracesListArgs
) -> list[dict[str, Any]]:
    """List recent traces for a service."""
    return await client.traces_list(args.service, args.limit)


async def traces_get_handler(
    client: ObservabilityClient, args: TracesGetArgs
) -> dict[str, Any] | None:
    """Fetch a specific trace by ID."""
    return await client.traces_get(args.trace_id)


HandlerType = Callable[
    [ObservabilityClient, Any],
    Coroutine[Any, Any, Any],
]


class ToolSpec:
    def __init__(
        self,
        name: str,
        description: str,
        input_schema: dict[str, Any],
        handler: HandlerType,
    ) -> None:
        self.name = name
        self.description = description
        self.input_schema = input_schema
        self.handler = handler

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "inputSchema": self.input_schema,
        }


# Create tool specs with explicit types
def create_tool_spec(
    name: str,
    description: str,
    input_schema: dict[str, Any],
    handler: HandlerType,
) -> ToolSpec:
    return ToolSpec(
        name=name,
        description=description,
        input_schema=input_schema,
        handler=handler,
    )


TOOLS_BY_NAME: dict[str, ToolSpec] = {
    "mcp_obs_logs_search": create_tool_spec(
        name="mcp_obs_logs_search",
        description="Search logs in VictoriaLogs by keyword and/or time range. "
        "Useful fields: service.name, severity, event, trace_id. "
        'Example query: _time:10m service.name:"Learning Management Service" severity:ERROR',
        input_schema={
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "LogsQL query string. Examples: "
                    "'_time:10m severity:ERROR', "
                    "'service.name:\"Learning Management Service\" severity:ERROR'",
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of results to return",
                    "default": 10,
                },
            },
            "required": ["query"],
        },
        handler=logs_search_handler,
    ),
    "mcp_obs_logs_error_count": create_tool_spec(
        name="mcp_obs_logs_error_count",
        description="Count error-level log entries per service over a time window. "
        "Useful for quickly checking if there are recent errors.",
        input_schema={
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "description": "Service name to filter by (e.g., 'Learning Management Service'). "
                    "If not provided, returns total error count.",
                },
                "time_window": {
                    "type": "string",
                    "description": "Time window for the query (e.g., '10m', '1h', '24h')",
                    "default": "1h",
                },
            },
        },
        handler=logs_error_count_handler,
    ),
    "mcp_obs_traces_list": create_tool_spec(
        name="mcp_obs_traces_list",
        description="List recent traces for a service from VictoriaTraces. "
        "Returns trace IDs and span summaries.",
        input_schema={
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "description": "Service name to list traces for (e.g., 'Learning Management Service')",
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of traces to return",
                    "default": 10,
                },
            },
            "required": ["service"],
        },
        handler=traces_list_handler,
    ),
    "mcp_obs_traces_get": create_tool_spec(
        name="mcp_obs_traces_get",
        description="Fetch a specific trace by its trace ID from VictoriaTraces. "
        "Returns the full trace with all spans and timing information.",
        input_schema={
            "type": "object",
            "properties": {
                "trace_id": {
                    "type": "string",
                    "description": "The trace ID (can be found in logs via the trace_id field)",
                },
            },
            "required": ["trace_id"],
        },
        handler=traces_get_handler,
    ),
}

TOOL_SPECS_LIST = list(TOOLS_BY_NAME.values())
