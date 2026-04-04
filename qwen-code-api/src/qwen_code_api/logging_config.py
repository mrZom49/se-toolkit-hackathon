"""Structured logging bootstrap for the Qwen Code API."""

from __future__ import annotations

import json
import logging
import sys
from datetime import datetime, timezone
from typing import Any, cast

from .config import settings


def _has_only_string_keys(value: object) -> bool:
    """Return True when all dictionary keys are strings."""
    if not isinstance(value, dict):
        return False
    mapping = cast(dict[Any, Any], value)
    for key in mapping:
        if not isinstance(key, str):
            return False
    return True


class JsonFormatter(logging.Formatter):
    """Format log records as structured JSON."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, object] = {
            "timestamp": datetime.fromtimestamp(
                record.created, timezone.utc
            ).isoformat().replace("+00:00", "Z"),
            "level": record.levelname,
            "logger": record.name,
        }

        message = record.getMessage()
        try:
            parsed: object = json.loads(message)
        except json.JSONDecodeError:
            payload["message"] = message
        else:
            if _has_only_string_keys(parsed):
                payload.update(cast(dict[str, object], parsed))
            else:
                payload["message"] = message

        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)

        return json.dumps(payload)


def configure_logging() -> None:
    """Configure fallback structured logging for local runs."""
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(JsonFormatter())
    logging.basicConfig(
        level=logging.DEBUG if settings.log_level == "debug" else logging.INFO,
        handlers=[handler],
        force=True,
    )


log = logging.getLogger("qwen_code_api")
