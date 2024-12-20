import os
from authlib.integrations.starlette_client import OAuth
from fastapi import Request
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OAuth configuration
oauth = OAuth()

oauth.register(
    name='github',
    client_id=os.getenv('GITHUB_CLIENT_ID', 'default_client_id'),
    client_secret=os.getenv('GITHUB_CLIENT_SECRET', 'default_client_secret'),
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'read:user'}
)

def get_github_redirect_uri(request: Request) -> str:
    """
    Generate the redirect URI for GitHub OAuth.

    Args:
        request (Request): The incoming FastAPI request.

    Returns:
        str: The redirect URI.
    """
    return request.url_for('auth')

def github_authorize_redirect(request: Request):
    """
    Initiates the GitHub OAuth authorization process.

    Args:
        request (Request): The incoming FastAPI request.

    Returns:
        Response: The redirection response to GitHub authorization.
    """
    redirect_uri = get_github_redirect_uri(request)
    return oauth.github.authorize_redirect(request, redirect_uri)

def github_fetch_user(request: Request):
    """
    Fetch the GitHub user profile after authorization.

    Args:
        request (Request): The incoming FastAPI request.

    Returns:
        dict: The user profile data from GitHub.
    """
    token = oauth.github.authorize_access_token(request)
    user = oauth.github.get('user', token=token)
    return user.json()
