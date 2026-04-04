"""Canonical package for the LMS MCP server."""

from mcp_lms.client import LMSClient
from mcp_lms.models import (
    CompletionRate,
    GroupPerformance,
    HealthResult,
    Item,
    Learner,
    PassRate,
    SyncResult,
    TimelineEntry,
    TopLearner,
)
from mcp_lms.settings import Settings
from mcp_lms.server import create_server, main

__all__ = [
    "CompletionRate",
    "GroupPerformance",
    "HealthResult",
    "Item",
    "Learner",
    "LMSClient",
    "PassRate",
    "Settings",
    "SyncResult",
    "TimelineEntry",
    "TopLearner",
    "create_server",
    "main",
]
