# backend/app/routers/backup.py

from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from src.app.core.tasks.database import backup_database
from src.celery_app import celery

router = APIRouter()


# Add async support
@router.get("/trigger-backup/")
async def trigger_backup():
    try:
        result = backup_database.delay()
        return JSONResponse({
            "task_id": result.id,
            "status_url": f"/tasks/{result.id}/status"
        })
    except celery.exceptions.OperationalError:
        raise HTTPException(503, "Backup service unavailable")
