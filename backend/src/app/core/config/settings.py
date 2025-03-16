# backend/app/config.py

import os

from pydantic import Field, RedisDsn, PostgresDsn, AmqpDsn, HttpUrl, ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application
    DEBUG: bool = False
    PROJECT_NAME: str = "MyApp"
    SECRET_KEY: str = Field(default_factory=lambda: os.urandom(32).hex())
    DOMAIN: str = "localhost"

    # Security
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 1 week
    CORS_ORIGINS: list[str] = ["*"]

    # GitHub OAuth
    GITHUB_CLIENT_ID: str
    GITHUB_CLIENT_SECRET: str
    GITHUB_CALLBACK_PATH: str = "/auth/callback"
    GITHUB_ACCESS_TOKEN_URL: HttpUrl
    GITHUB_AUTHORIZE_URL: HttpUrl
    GITHUB_API_BASE_URL: HttpUrl
    GITHUB_SCOPES: str

    # Database
    MARIADB_ROOT_PASSWORD: str
    MARIADB_HOST: str
    MARIADB_USER: str
    MARIADB_PASSWORD: str
    MARIADB_DATABASE: str

    # Frontend
    FRONTEND_URL: HttpUrl = "http://localhost:3000"

    # Database
    POSTGRES_URL: PostgresDsn = Field(
        default="postgresql+asyncpg://user:pass@localhost:5432/db"
    )

    # Redis
    REDIS_URL: RedisDsn = "redis://redis:6379/0"

    # Celery
    CELERY_BROKER_URL: AmqpDsn = "amqp://guest:guest@rabbitmq:5672//"
    CELERY_RESULT_BACKEND: RedisDsn = "redis://redis:6379/1"

    model_config = ConfigDict(
        env_file=".env.dev",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
