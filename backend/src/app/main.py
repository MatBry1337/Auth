# backend/app/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from src.app.core.config.settings import settings
from src.app.routers import auth, backup
from src.app.utils.logger import setup_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Improved lifespan management using contextlib"""
    logger = setup_logger()
    app.state.logger = logger
    logger.info("App starting...")
    try:
        yield
    finally:
        logger.info("App shutting down...")


app = FastAPI(lifespan=lifespan)

app.add_middleware(SessionMiddleware, secret_key=str(settings.SECRET_KEY))

# Improved CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in future might be ALLOWED_ORIGIN in settings
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"]
)

# Routers
app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(backup.router, prefix="/api/v1/backup")


@app.get("/health")
async def health_check():
    """Improved health check endpoint"""
    return {
        "status": "ok",
        "details": {
            "database": "connected",  # Add actual DB check
            "redis": "connected"  # Add actual Redis check
        }
    }
