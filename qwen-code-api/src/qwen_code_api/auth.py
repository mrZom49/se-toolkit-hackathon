"""Qwen OAuth credential management."""

import asyncio
import json
import time
from typing import Any

import httpx
from pydantic import BaseModel

from .config import settings
from .logging_config import log


class QwenCredentials(BaseModel):
    access_token: str = ""
    refresh_token: str = ""
    token_type: str = ""
    resource_url: str = ""
    expiry_date: int = 0


class AuthManager:
    """Manages Qwen OAuth credentials with automatic token refresh."""

    def __init__(self) -> None:
        self._credentials: QwenCredentials | None = None
        self._refresh_lock = False

    def load_credentials(self) -> QwenCredentials | None:
        if not settings.qwen_code_auth_use:
            return None
        if self._credentials is not None:
            return self._credentials
        try:
            self._credentials = QwenCredentials.model_validate_json(
                settings.creds_file.read_text()
            )
            return self._credentials
        except (FileNotFoundError, ValueError):
            return None

    @staticmethod
    def is_token_valid(creds: QwenCredentials | None) -> bool:
        if not creds or not creds.access_token or not creds.expiry_date:
            return False
        return (
            time.time() * 1000
            < creds.expiry_date - settings.token_refresh_buffer_s * 1000
        )

    async def refresh_token(
        self, creds: QwenCredentials, client: httpx.AsyncClient
    ) -> QwenCredentials:
        if not creds.refresh_token:
            raise RuntimeError(
                "No refresh token available. Re-authenticate with Qwen CLI."
            )

        log.info("Refreshing Qwen access token...")
        resp = await client.post(
            settings.qwen_oauth_token_url,
            data={
                "grant_type": "refresh_token",
                "refresh_token": creds.refresh_token,
                "client_id": settings.qwen_oauth_client_id,
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json",
            },
        )
        if resp.status_code != 200:
            raise RuntimeError(
                "Token refresh failed: "
                f"status={resp.status_code}, "
                f"content_type={resp.headers.get('content-type', '<missing>')}, "
                f"body={resp.text[:500]!r}"
            )

        try:
            token_data: dict[str, Any] = resp.json()
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                "Token refresh returned a non-JSON response: "
                f"status={resp.status_code}, "
                f"content_type={resp.headers.get('content-type', '<missing>')}, "
                f"body={resp.text[:500]!r}"
            ) from exc

        new_creds = QwenCredentials(
            access_token=token_data["access_token"],
            token_type=token_data.get("token_type", ""),
            refresh_token=token_data.get("refresh_token", creds.refresh_token),
            resource_url=token_data.get("resource_url", creds.resource_url),
            expiry_date=int(time.time() * 1000) + int(token_data["expires_in"]) * 1000,
        )
        settings.creds_file.write_text(new_creds.model_dump_json(indent=2))
        self._credentials = new_creds
        log.info("Token refreshed successfully")
        return new_creds

    async def get_valid_token(self, client: httpx.AsyncClient) -> str:
        if not settings.qwen_code_auth_use:
            return "bypass-token"
        creds = self.load_credentials()
        if not creds:
            raise RuntimeError(
                "No credentials found. Authenticate with Qwen CLI first."
            )
        if self.is_token_valid(creds):
            return creds.access_token

        if self._refresh_lock:
            for _ in range(50):
                await asyncio.sleep(0.1)
                creds = self.load_credentials()
                if creds and self.is_token_valid(creds):
                    return creds.access_token
            raise RuntimeError("Token refresh timed out")

        self._refresh_lock = True
        try:
            new_creds = await self.refresh_token(creds, client)
            return new_creds.access_token
        finally:
            self._refresh_lock = False

    @staticmethod
    def get_api_endpoint(creds: QwenCredentials | None) -> str:
        if creds and creds.resource_url:
            endpoint = creds.resource_url
            if not endpoint.startswith("http"):
                endpoint = f"https://{endpoint}"
            if not endpoint.endswith("/v1"):
                endpoint = endpoint.rstrip("/") + "/v1"
            return endpoint
        return settings.qwen_api_base
