# backend/celery_app.py

from celery import Celery

from src.app.core.config.settings import settings

celery = Celery(
    "backend",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

celery.conf.beat_schedule = {
    "backup-database-every-night": {
        "task": "app.tasks.database.backup_database",
        "schedule": 86400.0,  # Co 24 godzin
    },
}
celery.conf.timezone = "UTC"
