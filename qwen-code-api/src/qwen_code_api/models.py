"""Qwen model definitions, aliases, and token limits."""

from .config import settings

MODEL_ALIASES: dict[str, str] = {"qwen3.5-plus": "coder-model"}


def is_auth_error(status: int | None, message: str) -> bool:
    """Check if error is authentication-related (400/401/403/504 or auth message)."""
    if status in (400, 401, 403, 504):
        return True
    msg_lower = message.lower()
    return any(
        x in msg_lower
        for x in [
            "unauthorized",
            "forbidden",
            "token expired",
            "invalid api key",
            "invalid access token",
            "authentication",
            "access denied",
        ]
    )


def is_quota_error(status: int | None, message: str) -> bool:
    """Check if error is quota/rate limit related (429 or quota message)."""
    if status == 429:
        return True
    msg_lower = message.lower()
    return any(
        x in msg_lower
        for x in [
            "insufficient_quota",
            "quota exceeded",
            "rate limit",
            "too many requests",
        ]
    )


def is_validation_error(message: str) -> bool:
    """Check if error is a validation error."""
    return "validation error" in message.lower() or "invalid" in message.lower()


def make_error_response(
    message: str,
    error_type: str = "api_error",
    code: str | None = None,
) -> dict[str, dict[str, str | int] | dict[str, str]]:
    """Create OpenAI-compatible error response."""
    error: dict[str, str | int] = {
        "message": message,
        "type": error_type,
    }
    if code:
        error["code"] = code
    return {"error": error}


MODELS: list[dict[str, str | int]] = [
    {
        "id": "qwen3-coder-plus",
        "object": "model",
        "created": 1754686206,
        "owned_by": "qwen",
    },
    {
        "id": "qwen3-coder-flash",
        "object": "model",
        "created": 1754686206,
        "owned_by": "qwen",
    },
    {"id": "coder-model", "object": "model", "created": 1754686206, "owned_by": "qwen"},
    {
        "id": "vision-model",
        "object": "model",
        "created": 1754686206,
        "owned_by": "qwen",
    },
]

MODEL_MAX_TOKENS: dict[str, int] = {
    "vision-model": 32768,
    "qwen3-vl-plus": 32768,
    "qwen3-vl-max": 32768,
}


def resolve_model(model: str) -> str:
    return MODEL_ALIASES.get(model, model) or settings.default_model


def clamp_max_tokens(model: str, max_tokens: int) -> int:
    limit = MODEL_MAX_TOKENS.get(model)
    if limit and max_tokens > limit:
        return limit
    return max_tokens
