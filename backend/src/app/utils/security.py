from datetime import datetime, timedelta
from typing import Optional

import jwt
from pydantic import BaseModel
from src.app.core.config.settings import settings

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class TokenData(BaseModel):
    sub: str  # for example, the user id
    # Add other fields as needed


def create_access_token(data: TokenData, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.dict()
    now = datetime.utcnow()
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Add standard claims
    payload = {
        **to_encode,
        "exp": expire,
        "iat": now,
        "nbf": now,
    }
    encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
