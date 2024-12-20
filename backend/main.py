import os
import secrets
import subprocess
from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.sessions import SessionMiddleware

from celery import Celery

# Load environment variables
SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
CELERY_BACKEND_URL = os.getenv("CELERY_BACKEND_URL", "redis://redis:6379/0")

# Celery setup
celery = Celery("tasks", broker=CELERY_BROKER_URL, backend=CELERY_BACKEND_URL)

# FastAPI app setup
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)


@celery.task
def backup_database():
    """Task to backup the database."""
    backup_dir = "/backups"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file = f"{backup_dir}/db_backup_{timestamp}.sql"
    try:
        command = (
            f"mysqldump -h {os.getenv('MYSQL_HOST')} "
            f"-u {os.getenv('MYSQL_USER')} "
            f"-p{os.getenv('MYSQL_PASSWORD')} {os.getenv('MYSQL_DATABASE')} "
            f"> {backup_file}"
        )
        subprocess.run(command, shell=True, check=True)
        return f"Backup saved to {backup_file}"
    except subprocess.CalledProcessError as e:
        return f"Backup failed: {e}"


@app.get("/trigger-backup/")
def trigger_backup():
    """Manually trigger a database backup."""
    result = backup_database.delay()  # Trigger Celery task
    return JSONResponse({"message": "Backup initiated.", "task_id": result.id})


# Celery periodic task
celery.conf.beat_schedule = {
    "backup-database-every-night": {
        "task": "tasks.backup_database",
        "schedule": 86400.0,  # Every 24 hours
    },
}
celery.conf.timezone = "UTC"
