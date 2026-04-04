"""Router for learner endpoints."""

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel.ext.asyncio.session import AsyncSession

from lms_backend.database import get_session
from lms_backend.db.learners import read_learners, create_learner
from lms_backend.models.learner import Learner, LearnerCreate

router = APIRouter()


@router.get("/", response_model=list[Learner])
async def get_learners(
    enrolled_after: datetime | None = None,
    session: AsyncSession = Depends(get_session),
):
    """Get all learners, optionally filtered by enrollment date."""
    return await read_learners(session, enrolled_after)


@router.post("/", response_model=Learner, status_code=201)
async def post_learner(
    body: LearnerCreate,
    session: AsyncSession = Depends(get_session),
):
    """Create a new learner."""
    try:
        return await create_learner(
            session, external_id=body.external_id, student_group=body.student_group
        )
    except IntegrityError as exc:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=str(exc.orig),
        )
