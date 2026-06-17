from fastapi import APIRouter
from app.core.db import mongodb

router = APIRouter()


@router.get("/health")
async def health_check():

    try:
        await mongodb.database.command("ping")

        return {
            "status": "healthy",
            "mongodb": "connected"
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e)
        }