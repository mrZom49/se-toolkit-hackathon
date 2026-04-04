"""Tool schemas, handlers, and registry for the LMS MCP server."""

from __future__ import annotations

from collections.abc import Awaitable, Callable, Sequence
from dataclasses import dataclass

from mcp.types import Tool
from pydantic import BaseModel, Field

from mcp_lms.client import LMSClient


class NoArgs(BaseModel):
    """Empty input model for tools that only need server-side configuration."""


class LabQuery(BaseModel):
    lab: str = Field(description="Lab identifier, e.g. 'lab-04'.")


class TopLearnersQuery(LabQuery):
    limit: int = Field(
        default=5, ge=1, description="Max learners to return (default 5)."
    )


ToolPayload = BaseModel | Sequence[BaseModel]
ToolHandler = Callable[[LMSClient, BaseModel], Awaitable[ToolPayload]]


@dataclass(frozen=True, slots=True)
class ToolSpec:
    name: str
    description: str
    model: type[BaseModel]
    handler: ToolHandler

    def as_tool(self) -> Tool:
        schema = self.model.model_json_schema()
        schema.pop("$defs", None)
        schema.pop("title", None)
        return Tool(name=self.name, description=self.description, inputSchema=schema)


async def _health(client: LMSClient, _args: BaseModel) -> ToolPayload:
    return await client.health_check()


async def _labs(client: LMSClient, _args: BaseModel) -> ToolPayload:
    return await client.get_labs()


async def _learners(client: LMSClient, _args: BaseModel) -> ToolPayload:
    return await client.get_learners()


async def _pass_rates(client: LMSClient, args: BaseModel) -> ToolPayload:
    return await client.get_pass_rates(_require_lab_query(args).lab)


async def _timeline(client: LMSClient, args: BaseModel) -> ToolPayload:
    return await client.get_timeline(_require_lab_query(args).lab)


async def _groups(client: LMSClient, args: BaseModel) -> ToolPayload:
    return await client.get_groups(_require_lab_query(args).lab)


async def _top_learners(client: LMSClient, args: BaseModel) -> ToolPayload:
    query = _require_top_learners_query(args)
    return await client.get_top_learners(query.lab, limit=query.limit)


async def _completion_rate(client: LMSClient, args: BaseModel) -> ToolPayload:
    return await client.get_completion_rate(_require_lab_query(args).lab)


async def _sync_pipeline(client: LMSClient, _args: BaseModel) -> ToolPayload:
    return await client.sync_pipeline()


def _require_lab_query(args: BaseModel) -> LabQuery:
    if not isinstance(args, LabQuery):
        raise TypeError(f"Expected {LabQuery.__name__}, got {type(args).__name__}")
    return args


def _require_top_learners_query(args: BaseModel) -> TopLearnersQuery:
    if not isinstance(args, TopLearnersQuery):
        raise TypeError(
            f"Expected {TopLearnersQuery.__name__}, got {type(args).__name__}"
        )
    return args


TOOL_SPECS = (
    ToolSpec(
        "lms_health",
        "Check if the LMS backend is healthy and report the item count.",
        NoArgs,
        _health,
    ),
    ToolSpec("lms_labs", "List all labs available in the LMS.", NoArgs, _labs),
    ToolSpec(
        "lms_learners",
        "List all learners registered in the LMS.",
        NoArgs,
        _learners,
    ),
    ToolSpec(
        "lms_pass_rates",
        "Get pass rates (avg score and attempt count per task) for a lab.",
        LabQuery,
        _pass_rates,
    ),
    ToolSpec(
        "lms_timeline",
        "Get submission timeline (date + submission count) for a lab.",
        LabQuery,
        _timeline,
    ),
    ToolSpec(
        "lms_groups",
        "Get group performance (avg score + student count per group) for a lab.",
        LabQuery,
        _groups,
    ),
    ToolSpec(
        "lms_top_learners",
        "Get top learners by average score for a lab.",
        TopLearnersQuery,
        _top_learners,
    ),
    ToolSpec(
        "lms_completion_rate",
        "Get completion rate (passed / total) for a lab.",
        LabQuery,
        _completion_rate,
    ),
    ToolSpec(
        "lms_sync_pipeline",
        "Trigger the LMS sync pipeline. May take a moment.",
        NoArgs,
        _sync_pipeline,
    ),
)
TOOLS_BY_NAME = {spec.name: spec for spec in TOOL_SPECS}
