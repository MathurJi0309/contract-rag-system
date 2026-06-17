from fastapi import APIRouter

from app.modules.documents.router import router as document_router
from app.modules.query.router import router as query_router
from app.modules.users.router import user_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    user_router,
    prefix="/user",
    tags=["Users"]
)
api_router.include_router(
    document_router,
    prefix="/documents",
    tags=["Documents"]
)

api_router.include_router(
    query_router,
    prefix="/query",
    tags=["Query"]
)
