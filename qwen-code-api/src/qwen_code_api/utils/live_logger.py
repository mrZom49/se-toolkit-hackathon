"""Structured event logger using standard logging."""

import logging
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


class LiveLogger:
    """Structured event logger using standard logging."""

    @staticmethod
    def _emit(level: int, payload: dict[str, object]) -> None:
        """Emit a single structured log record with extra attributes."""
        event = str(payload.get("event", "event"))
        logger.log(level, event, extra=payload)

    def proxy_request(
        self,
        request_id: str,
        model: str,
        account_id: str | None,
        token_count: int,
        request_num: int | None = None,
        is_streaming: bool = False,
    ) -> None:
        """Log incoming proxy request."""
        self._emit(
            logging.INFO,
            {
                "event": "request",
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "request_id": request_id,
                "model": model,
                "account_id": account_id,
                "token_count": token_count,
                "is_streaming": is_streaming,
                "request_num": request_num,
            }
        )

    def proxy_response(
        self,
        request_id: str,
        status_code: int,
        account_id: str | None,
        latency_ms: int,
        input_tokens: int | None = None,
        output_tokens: int | None = None,
        qwen_id: str | None = None,
    ) -> None:
        """Log proxy response."""
        self._emit(
            logging.INFO,
            {
                "event": "response",
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "request_id": request_id,
                "status_code": status_code,
                "account_id": account_id,
                "latency_ms": latency_ms,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "qwen_id": qwen_id,
            }
        )

    def proxy_error(
        self,
        request_id: str,
        status_code: int,
        account_id: str | None,
        error_message: str,
    ) -> None:
        """Log proxy error."""
        self._emit(
            logging.ERROR,
            {
                "event": "error",
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "request_id": request_id,
                "status_code": status_code,
                "account_id": account_id,
                "error_message": error_message,
            }
        )

    def auth_initiated(self, device_code: str) -> None:
        """Log authentication initiated."""
        self._emit(
            logging.INFO,
            {
                "event": "auth",
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "action": "initiated",
                "device_code": device_code,
            }
        )

    def auth_completed(self, account_id: str) -> None:
        """Log authentication completed."""
        self._emit(
            logging.INFO,
            {
                "event": "auth",
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "action": "completed",
                "account_id": account_id,
            }
        )

    def account_refreshed(self, account_id: str, status: str) -> None:
        """Log account token refresh."""
        self._emit(
            logging.INFO,
            {
                "event": "auth",
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "action": "refreshed",
                "account_id": account_id,
                "status": status,
            }
        )

    def account_added(self, account_id: str) -> None:
        """Log account added."""
        self._emit(
            logging.INFO,
            {
                "event": "auth",
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "action": "added",
                "account_id": account_id,
            }
        )

    def account_removed(self, account_id: str) -> None:
        """Log account removed."""
        self._emit(
            logging.INFO,
            {
                "event": "auth",
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "action": "removed",
                "account_id": account_id,
            }
        )

    def server_started(self, host: str, port: int) -> None:
        """Log server startup."""
        self._emit(
            logging.INFO,
            {
                "event": "server",
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "action": "started",
                "host": host,
                "port": port,
            }
        )

    def shutdown(self, reason: str) -> None:
        """Log server shutdown."""
        self._emit(
            logging.INFO,
            {
                "event": "server",
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "action": "shutdown",
                "reason": reason,
            }
        )


# Global instance
live_logger = LiveLogger()
