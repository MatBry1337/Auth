from celery import Celery
from celery.schedules import crontab

app = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

@app.task
def backup_database():
    import subprocess
    from datetime import datetime

    backup_file = f"/backups/db_backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.sql"
    command = f"mysqldump -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE > {backup_file}"
    subprocess.run(command, shell=True, check=True)

app.conf.beat_schedule = {
    "backup-database-every-night": {
        "task": "tasks.backup_database",
        "schedule": crontab(hour=2, minute=0),  # Runs every day at 2:00 AM
    },
}
app.conf.timezone = "UTC"
