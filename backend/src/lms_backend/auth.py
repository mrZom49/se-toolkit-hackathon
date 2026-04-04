"""API key authentication dependency."""

import logging

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from lms_backend.settings import settings

logger = logging.getLogger(__name__)

security = HTTPBearer()


def verify_api_key(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> str:
    """Verify the API key from the Authorization header.

    Expects: Authorization: Bearer <API_KEY>
    Returns the key string if valid.
    Raises 401 if invalid.
    """
    if credentials.credentials != settings.api_key:
        logger.warning("auth_failure", extra={"event": "auth_failure"})
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    logger.info("auth_success", extra={"event": "auth_success"})
    return credentials.credentials
