"""End-to-end tests for the GET /items endpoint."""

import httpx


def test_get_items_returns_200(client: httpx.Client) -> None:
    response = client.get("/items/")
    assert response.status_code == 200


def test_get_items_response_is_a_list(client: httpx.Client) -> None:
    response = client.get("/items/")
    assert isinstance(response.json(), list)
