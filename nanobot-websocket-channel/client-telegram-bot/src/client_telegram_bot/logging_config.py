"""Structured logging setup for the Telegram bot."""

from __future__ import annotations

import json
import logging
from datetime import UTC, datetime


def event_fields(event: str, **fields: object) -> dict[str, object]:
    """Build a structured logging payload with a consistent event field."""
    return {"event": event, **fields}


class JsonFormatter(logging.Formatter):
    """Emit structured JSON logs for OTEL export and local debugging."""

    _RESERVED = {
        "args",
        "asctime",
        "created",
        "exc_info",
        "exc_text",
        "filename",
        "funcName",
        "levelname",
        "levelno",
        "lineno",
        "module",
        "msecs",
        "message",
        "msg",
        "name",
        "pathname",
        "process",
        "processName",
        "relativeCreated",
        "stack_info",
        "thread",
        "threadName",
        "taskName",
    }

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, object] = {
            "timestamp": datetime.fromtimestamp(record.created, UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        for key, value in record.__dict__.items():
            if key in self._RESERVED or key.startswith("_"):
                continue
            payload[key] = value if self._is_jsonable(value) else str(value)
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=True)

    @staticmethod
    def _is_jsonable(value: object) -> bool:
        try:
            json.dumps(value)
        except TypeError:
            return False
        return True


def configure_logging() -> None:
    """Configure process-wide structured logging."""
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    logging.basicConfig(level=logging.INFO, handlers=[handler], force=True)
