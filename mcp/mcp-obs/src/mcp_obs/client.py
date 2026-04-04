"""Observability MCP client for VictoriaLogs and VictoriaTraces."""

import logging
from typing import Any

import httpx

from mcp_obs.settings import settings

logger = logging.getLogger(__name__)


class ObservabilityClient:
    def __init__(self) -> None:
        self.victorialogs_url = settings.victorialogs_url
        self.victoriatraces_url = settings.victoriatraces_url

    async def logs_search(
        self,
        query: str,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Search logs in VictoriaLogs."""
        url = f"{self.victorialogs_url}/select/logsql/query"
        params = {"query": query, "limit": limit}
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            lines = response.text.strip().split("\n")
            results = []
            for line in lines:
                if line.strip():
                    try:
                        results.append(line)
                    except Exception:
                        pass
            return results

    async def logs_error_count(
        self,
        service: str | None = None,
        time_window: str = "1h",
    ) -> dict[str, int]:
        """Count errors per service over a time window."""
        query = f"_time:{time_window} severity:ERROR"
        if service:
            query = f'{query} service.name:"{service}"'
        url = f"{self.victorialogs_url}/select/logsql/query"
        params = {"query": query, "limit": 1000}
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            lines = response.text.strip().split("\n")
            count = sum(1 for line in lines if line.strip())
            if service:
                return {service: count}
            services: dict[str, int] = {}
            for line in lines:
                if line.strip():
                    services["total"] = count
                    break
            return services

    async def traces_list(
        self,
        service: str,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """List recent traces for a service."""
        url = f"{self.victoriatraces_url}/select/jaeger/api/traces"
        params = {"service": service, "limit": limit}
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("data", [])

    async def traces_get(
        self,
        trace_id: str,
    ) -> dict[str, Any] | None:
        """Fetch a specific trace by ID."""
        url = f"{self.victoriatraces_url}/select/jaeger/api/traces/{trace_id}"
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url)
            if response.status_code == 404:
                return None
            response.raise_for_status()
            data = response.json()
            traces = data.get("data", [])
            return traces[0] if traces else None
