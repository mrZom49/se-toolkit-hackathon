"""FastAPI application assembly — lifespan, middleware, routers."""

import time
from contextlib import asynccontextmanager
from typing import AsyncIterator

import httpx
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .auth import AuthManager
from .config import settings
from .logging_config import configure_logging, log
from .routes import chat, health, models
from .utils.live_logger import live_logger

configure_logging()


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    _app.state.auth = AuthManager()
    _app.state.http_client = httpx.AsyncClient(timeout=httpx.Timeout(300, connect=10))
    _app.state.request_count = 0
    _app.state.start_time = time.time()

    live_logger.server_started(host=settings.address, port=settings.port)
    creds = _app.state.auth.load_credentials()
    if creds:
        valid = AuthManager.is_token_valid(creds)
        log.info("Default credentials: %s", "valid" if valid else "expired/invalid")
    else:
        log.warning("No credentials found")

    yield

    live_logger.shutdown("Server stopping")
    await _app.state.http_client.aclose()


app = FastAPI(title="Qwen Code API (Python)", lifespan=lifespan)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,  # type: ignore[arg-type]
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(models.router)
app.include_router(health.router)


def validate_api_key(
    x_api_key: str | None = Header(None),
    authorization: str | None = Header(None),
) -> None:
    if settings.api_keys is None:
        return
    key = x_api_key
    if not key and authorization:
        key = (
            authorization.removeprefix("Bearer ").strip()
            if authorization.startswith("Bearer ")
            else authorization.strip()
        )
    if not key or key not in settings.api_keys:
        raise HTTPException(
            status_code=401,
            detail={
                "error": {
                    "message": "Invalid or missing API key",
                    "type": "authentication_error",
                }
            },
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.address, port=settings.port)
