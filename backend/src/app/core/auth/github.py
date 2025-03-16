# backend/app/auth/github.py
import logging

from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import HTTPException
from starlette.requests import Request

from src.app.core.config.settings import settings

logger = logging.getLogger("auth.github")

oauth = OAuth()

oauth.register(
    name="github",
    client_id=settings.GITHUB_CLIENT_ID,
    client_secret=settings.GITHUB_CLIENT_SECRET,
    access_token_url=str(settings.GITHUB_ACCESS_TOKEN_URL),
    authorize_url=str(settings.GITHUB_AUTHORIZE_URL),
    api_base_url=str(settings.GITHUB_API_BASE_URL),
    client_kwargs={"scope": settings.GITHUB_SCOPES},
)


async def github_authorize_redirect(request: Request):
    """Dynamic OAuth redirect URI based on environment"""
    try:
        redirect_uri = "http://localhost:8000/api/v1/auth/callback"
        return await oauth.github.authorize_redirect(request, redirect_uri)
    except OAuthError as e:
        logger.error(f"OAuth initialization failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="OAuth service configuration error"
        )


async def github_fetch_user(request: Request):
    """Exchange code for token and fetch user data with error handling"""
    try:
        token = await oauth.github.authorize_access_token(request)
        if not token or "access_token" not in token:
            logger.warning("Invalid token response from GitHub")
            raise HTTPException(400, "Invalid authorization code")

        resp = await oauth.github.get("user", token=token)
        resp.raise_for_status()
        return resp.json()
    except OAuthError as e:
        logger.error(f"OAuth exchange failed: {str(e)}")
        raise HTTPException(502, "OAuth provider unreachable")
