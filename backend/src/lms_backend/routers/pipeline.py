"""Router for the ETL pipeline endpoint."""

from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from lms_backend.database import get_session
from lms_backend.etl import sync

router = APIRouter()


@router.post("/sync")
async def post_sync(session: AsyncSession = Depends(get_session)):
    """Trigger a data sync from the autochecker API.

    Fetches the latest items and logs, loads them into the database,
    and returns a summary of what was synced.
    """
    return await sync(session)
