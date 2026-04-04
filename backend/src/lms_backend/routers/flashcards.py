"""Router for flashcard endpoints."""

import logging

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel.ext.asyncio.session import AsyncSession

from lms_backend.database import get_session
from lms_backend.db.flashcards import (
    create_card,
    create_deck,
    read_cards,
    read_deck,
    read_decks,
)
from lms_backend.models.flashcard import (
    CardCreate,
    CardRead,
    DeckCreate,
    DeckRead,
)

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/decks", response_model=list[DeckRead])
async def get_decks(session: AsyncSession = Depends(get_session)):
    """Get all decks."""
    try:
        return await read_decks(session)
    except Exception as exc:
        logger.warning(
            "decks_list_failed",
            extra={"event": "decks_list_failed", "error": str(exc)},
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Backend error: {exc}",
        ) from exc


@router.post("/decks", response_model=DeckRead, status_code=201)
async def post_deck(body: DeckCreate, session: AsyncSession = Depends(get_session)):
    """Create a new deck."""
    try:
        return await create_deck(session, name=body.name)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Failed to create deck",
        )


@router.get("/decks/{deck_id}/cards", response_model=list[CardRead])
async def get_cards(deck_id: int, session: AsyncSession = Depends(get_session)):
    """Get all cards for a deck."""
    deck = await read_deck(session, deck_id)
    if deck is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Deck not found"
        )
    try:
        return await read_cards(session, deck_id)
    except Exception as exc:
        logger.warning(
            "cards_list_failed",
            extra={"event": "cards_list_failed", "error": str(exc)},
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Backend error: {exc}",
        ) from exc


@router.post("/decks/{deck_id}/cards", response_model=CardRead, status_code=201)
async def post_card(
    deck_id: int, body: CardCreate, session: AsyncSession = Depends(get_session)
):
    """Create a new card in a deck."""
    deck = await read_deck(session, deck_id)
    if deck is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Deck not found"
        )
    try:
        return await create_card(session, deck_id, body.question, body.answer)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Failed to create card",
        )
