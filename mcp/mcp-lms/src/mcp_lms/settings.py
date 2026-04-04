"""Runtime settings for the LMS MCP server."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Settings:
    base_url: str
    api_key: str


def resolve_api_key() -> str:
    for name in ("NANOBOT_LMS_API_KEY", "LMS_API_KEY"):
        value = os.environ.get(name, "").strip()
        if value:
            return value
    raise RuntimeError(
        "LMS API key not configured. Set NANOBOT_LMS_API_KEY or LMS_API_KEY."
    )


def resolve_base_url(base_url: str | None = None) -> str:
    value = (base_url or os.environ.get("NANOBOT_LMS_BACKEND_URL", "")).strip()
    if not value:
        raise RuntimeError(
            "LMS backend URL not configured. Pass it as: python -m mcp_lms <base_url>"
        )
    return value


def resolve_settings(base_url: str | None = None) -> Settings:
    return Settings(base_url=resolve_base_url(base_url), api_key=resolve_api_key())
