# backend/app/tasks/database.py

import os
import subprocess
from datetime import datetime

from celery import shared_task

from src.app.core.config.settings import settings


@shared_task
def backup_database():
    """Task to backup the database."""
    backup_dir = "/backups"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    backup_file = f"{backup_dir}/db_backup_{timestamp}.sql"
    try:
        command = (
            f"mysqldump -h {settings.MYSQL_HOST} "
            f"-u {settings.MYSQL_USER} "
            f"-p{settings.MYSQL_PASSWORD} {settings.MYSQL_DATABASE} "
            f"> {backup_file}"
        )
        subprocess.run(command, shell=True, check=True)
        return f"Backup saved to {backup_file}"
    except subprocess.CalledProcessError as e:
        return f"Backup failed: {e}"
