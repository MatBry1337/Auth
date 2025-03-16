# backend/app/routers/auth.py
from fastapi import APIRouter, Request

from src.app.core.auth.github import github_authorize_redirect, github_fetch_user

router = APIRouter()


@router.get("")
async def auth_redirect_endpoint(request: Request):
    request.app.state.logger.info("Authorizing GitHub")
    return await github_authorize_redirect(request)


@router.get("/callback")
async def auth_callback_endpoint(request: Request):
    # Step 2: GitHub redirects here with 'code' and 'state'
    user = await github_fetch_user(request)  # get user info from GitHub
    # Extract the username from the user data; GitHub returns the username under 'login'
    username = user.get("login", "Unknown User")
    # Optionally log or print the entire user object for debugging:
    request.app.state.logger.info(f"Authenticated GitHub user: {username}")
    # Return a response including the username
    return {"message": f"Welcome, {username}!"}
