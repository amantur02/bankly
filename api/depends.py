from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from sqlalchemy.orm import Session
from starlette import status
from jose import jwt

from core.config import settings
from core.constants import JWT_ALGORITHM, INVALID_AUTHENTICATION_CREDENTIALS
from resource_access.db_session import AsyncSessionLocal
from schemas.auth_schemas import TokenPayload

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.api_path}/auth/login/"
)


async def get_session() -> Session:
    session = AsyncSessionLocal()
    try:
        yield session
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()


async def get_token_data(token: str = Depends(oauth2_schema)) -> TokenPayload:
    try:
        payload = jwt.decode(
            token,
            settings.access_token_secret_key,
            algorithms=[JWT_ALGORITHM],
        )
        return TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=INVALID_AUTHENTICATION_CREDENTIALS,
            headers={"WWW-Authenticate": "Bearer"},
        )

