"""GET /v1/models — list available Qwen models."""

from fastapi import APIRouter, Header

from ..models import MODELS

router = APIRouter()


@router.get("/v1/models")
async def list_models(
    x_api_key: str | None = Header(None),
    authorization: str | None = Header(None),
) -> dict[str, str | list[dict[str, str | int]]]:
    from ..main import validate_api_key

    validate_api_key(x_api_key, authorization)
    return {"object": "list", "data": MODELS}
