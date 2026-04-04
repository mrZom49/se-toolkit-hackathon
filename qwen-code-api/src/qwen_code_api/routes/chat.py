"""POST /v1/chat/completions — proxy to DashScope with retry and streaming."""

import asyncio
import time
import uuid
from typing import Any

import httpx
from fastapi import APIRouter, Header, Request
from fastapi.responses import JSONResponse, StreamingResponse

from ..auth import AuthManager
from ..config import settings
from ..headers import build_headers
from ..logging_config import log
from ..models import (
    clamp_max_tokens,
    is_auth_error,
    is_quota_error,
    is_validation_error,
    make_error_response,
    resolve_model,
)
from ..utils.live_logger import live_logger

router = APIRouter()


async def _handle_regular(
    client: httpx.AsyncClient,
    url: str,
    payload: dict[str, Any],
    headers: dict[str, str],
    request_id: str,
    start_time: float,
) -> JSONResponse:
    resp = await client.post(url, json=payload, headers=headers)
    resp.raise_for_status()

    # Log response
    latency_ms = int((time.time() - start_time) * 1000)
    data = resp.json()
    input_tokens = data.get("usage", {}).get("prompt_tokens")
    output_tokens = data.get("usage", {}).get("completion_tokens")
    qwen_id = data.get("id")

    if settings.log_requests:
        live_logger.proxy_response(
            request_id=request_id,
            status_code=resp.status_code,
            account_id=None,
            latency_ms=latency_ms,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            qwen_id=qwen_id,
        )

    return JSONResponse(content=data)


async def _handle_streaming(
    client: httpx.AsyncClient,
    url: str,
    payload: dict[str, Any],
    headers: dict[str, str],
    request_id: str,
    start_time: float,
) -> StreamingResponse:
    req = client.build_request("POST", url, json=payload, headers=headers)
    resp = await client.send(req, stream=True)
    resp.raise_for_status()

    # Log streaming start
    latency_ms = int((time.time() - start_time) * 1000)
    if settings.log_requests:
        live_logger.proxy_response(
            request_id=request_id,
            status_code=resp.status_code,
            account_id=None,
            latency_ms=latency_ms,
        )

    async def generate():
        try:
            async for chunk in resp.aiter_bytes():
                yield chunk
        finally:
            await resp.aclose()

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
        },
    )


@router.post("/v1/chat/completions", response_model=None)
async def chat_completions(
    request: Request,
    x_api_key: str | None = Header(None),
    authorization: str | None = Header(None),
) -> JSONResponse | StreamingResponse:
    from ..main import validate_api_key

    validate_api_key(x_api_key, authorization)

    auth: AuthManager = request.app.state.auth
    client: httpx.AsyncClient = request.app.state.http_client
    request.app.state.request_count += 1

    body: dict[str, Any] = await request.json()
    is_streaming: bool = body.get("stream", False)
    model = resolve_model(body.get("model", settings.default_model))
    max_tokens = clamp_max_tokens(model, body.get("max_tokens", 65536))

    # Generate request ID and log request
    request_id = str(uuid.uuid4())
    start_time = time.time()
    messages = body.get("messages", [])
    token_count = len(str(messages)) // 4  # Rough approximation

    if settings.log_requests:
        live_logger.proxy_request(
            request_id=request_id,
            model=model,
            account_id=None,
            token_count=token_count,
            is_streaming=is_streaming,
        )

    access_token = await auth.get_valid_token(client)
    creds = auth.load_credentials()
    url = f"{auth.get_api_endpoint(creds)}/chat/completions"
    headers = build_headers(access_token, streaming=is_streaming)
    if not settings.qwen_code_auth_use:
        headers["authorization"] = f"Bearer {settings.qwen_code_api_key}"
        url = f"{settings.qwen_api_base}/chat/completions"

    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
        "stream": is_streaming,
        "temperature": body.get("temperature", 0.7),
        "max_tokens": max_tokens,
    }
    for field in (
        "top_p",
        "top_k",
        "repetition_penalty",
        "tools",
        "tool_choice",
        "reasoning",
    ):
        if field in body:
            payload[field] = body[field]

    if is_streaming:
        payload["stream_options"] = {"include_usage": True}

    last_error: Exception | None = None
    last_status: int | None = None
    for attempt in range(1, settings.max_retries + 1):
        try:
            if is_streaming:
                return await _handle_streaming(
                    client, url, payload, headers, request_id, start_time
                )
            else:
                return await _handle_regular(
                    client, url, payload, headers, request_id, start_time
                )
        except httpx.HTTPStatusError as exc:
            last_error = exc
            status = exc.response.status_code
            last_status = status

            # Check for validation errors first (return 400, don't retry)
            error_message = str(exc)
            if is_validation_error(error_message):
                log.warning(
                    "Validation error (status %d): %s", status, error_message[:100]
                )
                if settings.log_requests:
                    live_logger.proxy_error(
                        request_id=request_id,
                        status_code=status,
                        account_id=None,
                        error_message=error_message,
                    )
                return JSONResponse(
                    status_code=400,
                    content=make_error_response(
                        error_message,
                        error_type="validation_error",
                        code="invalid_request",
                    ),
                )

            # Retry on server errors and rate limits
            if status in (500, 429) and attempt < settings.max_retries:
                log.warning(
                    "Retry %d/%d (status %d)", attempt, settings.max_retries, status
                )
                await asyncio.sleep(settings.retry_delay_s * attempt)
                continue

            # Auth errors trigger token refresh
            if is_auth_error(status, error_message):
                try:
                    log.info("Auth error %d, refreshing token...", status)
                    creds = auth.load_credentials()
                    if creds:
                        new_creds = await auth.refresh_token(creds, client)
                        headers = build_headers(
                            new_creds.access_token, streaming=is_streaming
                        )
                        if is_streaming:
                            return await _handle_streaming(
                                client, url, payload, headers, request_id, start_time
                            )
                        else:
                            return await _handle_regular(
                                client, url, payload, headers, request_id, start_time
                            )
                except Exception as refresh_err:
                    log.error("Token refresh failed: %s", str(refresh_err))
                    if settings.log_requests:
                        live_logger.proxy_error(
                            request_id=request_id,
                            status_code=401,
                            account_id=None,
                            error_message="Token refresh failed",
                        )
                    # Return auth error instead of generic 500
                    return JSONResponse(
                        status_code=401,
                        content=make_error_response(
                            "Authentication failed. Please re-authenticate with Qwen CLI.",
                            error_type="authentication_error",
                            code="invalid_token",
                        ),
                    )
            break

        except Exception as exc:
            last_error = exc
            error_message = str(exc)

            # Check for validation errors
            if is_validation_error(error_message):
                log.warning("Validation error: %s", error_message[:100])
                if settings.log_requests:
                    live_logger.proxy_error(
                        request_id=request_id,
                        status_code=400,
                        account_id=None,
                        error_message=error_message,
                    )
                return JSONResponse(
                    status_code=400,
                    content=make_error_response(
                        error_message,
                        error_type="validation_error",
                        code="invalid_request",
                    ),
                )

            # Retry on generic errors
            if attempt < settings.max_retries:
                log.warning(
                    "Retry %d/%d (error: %s)",
                    attempt,
                    settings.max_retries,
                    error_message[:50],
                )
                await asyncio.sleep(settings.retry_delay_s * attempt)
                continue
            break

    # Build appropriate error response based on error type
    error_msg = str(last_error) if last_error else "Unknown error"

    if is_validation_error(error_msg):
        if settings.log_requests:
            live_logger.proxy_error(
                request_id=request_id,
                status_code=400,
                account_id=None,
                error_message=error_msg,
            )
        return JSONResponse(
            status_code=400,
            content=make_error_response(
                error_msg, error_type="validation_error", code="invalid_request"
            ),
        )

    if is_quota_error(last_status, error_msg):
        if settings.log_requests:
            live_logger.proxy_error(
                request_id=request_id,
                status_code=429,
                account_id=None,
                error_message=error_msg,
            )
        return JSONResponse(
            status_code=429,
            content=make_error_response(
                "Rate limit or quota exceeded. Please try again later.",
                error_type="rate_limit_exceeded",
                code="rate_limit_exceeded",
            ),
        )

    if is_auth_error(last_status, error_msg):
        if settings.log_requests:
            live_logger.proxy_error(
                request_id=request_id,
                status_code=401,
                account_id=None,
                error_message=error_msg,
            )
        return JSONResponse(
            status_code=401,
            content=make_error_response(
                "Authentication failed. Please re-authenticate with Qwen CLI.",
                error_type="authentication_error",
                code="invalid_token",
            ),
        )

    # Default: generic API error
    if settings.log_requests:
        live_logger.proxy_error(
            request_id=request_id,
            status_code=500,
            account_id=None,
            error_message=error_msg,
        )
    return JSONResponse(
        status_code=500,
        content=make_error_response(error_msg, error_type="api_error"),
    )
