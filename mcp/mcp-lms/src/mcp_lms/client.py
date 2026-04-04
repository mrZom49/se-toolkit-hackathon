"""Async HTTP client for the LMS backend API."""

from __future__ import annotations

from typing import Any, TypeVar

import httpx
from pydantic import BaseModel
from mcp_lms.models import (
    CompletionRate,
    GroupPerformance,
    HealthResult,
    Item,
    Learner,
    PassRate,
    SyncResult,
    TimelineEntry,
    TopLearner,
)


ModelT = TypeVar("ModelT", bound=BaseModel)


class LMSClient:
    """Client for the LMS backend API."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        *,
        http_client: httpx.AsyncClient | None = None,
        timeout: float = 10.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self._owns_client = http_client is None
        self._http_client = http_client or httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout,
        )

    async def __aenter__(self) -> LMSClient:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        if self._owns_client:
            await self._http_client.aclose()

    async def _request_json(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, str | int] | None = None,
    ) -> Any:
        response = await self._http_client.request(method, path, params=params)
        response.raise_for_status()
        return response.json()

    async def _get_list(
        self,
        path: str,
        model: type[ModelT],
        *,
        params: dict[str, str | int] | None = None,
    ) -> list[ModelT]:
        payload = await self._request_json("GET", path, params=params)
        return [model.model_validate(item) for item in payload]

    async def _get_model(
        self,
        path: str,
        model: type[ModelT],
        *,
        params: dict[str, str | int] | None = None,
    ) -> ModelT:
        payload = await self._request_json("GET", path, params=params)
        return model.model_validate(payload)

    async def _post_model(self, path: str, model: type[ModelT]) -> ModelT:
        payload = await self._request_json("POST", path)
        return model.model_validate(payload)

    async def health_check(self) -> HealthResult:
        try:
            items = await self.get_items()
            return HealthResult(status="healthy", item_count=len(items))
        except httpx.ConnectError:
            return HealthResult(
                status="unhealthy", error=f"connection refused ({self.base_url})"
            )
        except httpx.HTTPStatusError as error:
            return HealthResult(
                status="unhealthy", error=f"HTTP {error.response.status_code}"
            )
        except Exception as error:
            return HealthResult(status="unhealthy", error=str(error))

    async def get_items(self) -> list[Item]:
        return await self._get_list("/items/", Item)

    async def get_labs(self) -> list[Item]:
        return [item for item in await self.get_items() if item.type == "lab"]

    async def get_learners(self) -> list[Learner]:
        return await self._get_list("/learners/", Learner)

    async def get_pass_rates(self, lab: str) -> list[PassRate]:
        return await self._get_list(
            "/analytics/pass-rates",
            PassRate,
            params={"lab": lab},
        )

    async def get_timeline(self, lab: str) -> list[TimelineEntry]:
        return await self._get_list(
            "/analytics/timeline",
            TimelineEntry,
            params={"lab": lab},
        )

    async def get_groups(self, lab: str) -> list[GroupPerformance]:
        return await self._get_list(
            "/analytics/groups",
            GroupPerformance,
            params={"lab": lab},
        )

    async def get_top_learners(self, lab: str, limit: int = 5) -> list[TopLearner]:
        return await self._get_list(
            "/analytics/top-learners",
            TopLearner,
            params={"lab": lab, "limit": limit},
        )

    async def get_completion_rate(self, lab: str) -> CompletionRate:
        return await self._get_model(
            "/analytics/completion-rate",
            CompletionRate,
            params={"lab": lab},
        )

    async def sync_pipeline(self) -> SyncResult:
        return await self._post_model("/pipeline/sync", SyncResult)
