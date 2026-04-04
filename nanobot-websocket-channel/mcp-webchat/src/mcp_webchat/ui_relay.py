"""Client for the internal WebChat structured-message relay."""

from __future__ import annotations

from typing import Any

import httpx
from nanobot_channel_protocol.schemas import OutboundPayload
from pydantic import TypeAdapter


_OUTBOUND_ADAPTER: TypeAdapter[OutboundPayload] = TypeAdapter(OutboundPayload)


class UIRelayClient:
    """Post validated structured payloads to the local WebChat relay."""

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def _client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(
            headers={"Authorization": f"Bearer {self.token}"},
            timeout=10.0,
        )

    async def send(self, *, chat_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        parsed = _OUTBOUND_ADAPTER.validate_python(payload)
        async with self._client() as client:
            response = await client.post(
                f"{self.base_url}/ui-message",
                json={"chat_id": chat_id, "payload": parsed.model_dump(mode="json")},
            )
            response.raise_for_status()
            return response.json()
