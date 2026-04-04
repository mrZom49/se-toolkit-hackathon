"""GET /health — server health and token status."""

import time
from typing import Any

from fastapi import APIRouter, Request

from ..auth import AuthManager

router = APIRouter()


@router.get("/health")
async def health(request: Request) -> dict[str, Any]:
    auth: AuthManager = request.app.state.auth
    creds = auth.load_credentials()
    token_status = "no_credentials"
    expires_in: str | None = None

    if creds and creds.expiry_date:
        minutes_left = (creds.expiry_date - time.time() * 1000) / 60000
        if minutes_left < 0:
            token_status = "expired"
        elif minutes_left < 30:
            token_status = "expiring_soon"
        else:
            token_status = "healthy"
        expires_in = f"{max(0.0, minutes_left):.1f} minutes"

    return {
        "status": "ok",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "default_account": {
            "status": token_status,
            "expires_in": expires_in,
        },
        "total_requests": request.app.state.request_count,
        "uptime_seconds": round(time.time() - request.app.state.start_time, 1),
    }
