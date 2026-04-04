"""Shared fixtures for end-to-end tests."""

import os

import httpx
import pytest


@pytest.fixture(scope="session")
def api_base_url() -> str:
    url = os.environ.get("GATEWAY_BASE_URL", "")
    if not url:
        pytest.skip("GATEWAY_BASE_URL environment variable is not set")
    return url.rstrip("/")


@pytest.fixture(scope="session")
def api_key() -> str:
    key = os.environ.get("LMS_API_KEY", "")
    if not key:
        pytest.skip("LMS_API_KEY environment variable is not set")
    return key


@pytest.fixture(scope="session")
def client(api_base_url: str, api_key: str) -> httpx.Client:
    return httpx.Client(
        base_url=api_base_url,
        headers={"Authorization": f"Bearer {api_key}"},
    )
