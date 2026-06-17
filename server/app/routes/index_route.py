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


from pathlib import Path

UPLOAD_DIR = Path(__file__).resolve().parents[2] / "data" / "uploads"

print("UPLOAD_DIR =", UPLOAD_DIR)

@api_router.get("/documents/status")
async def documents_status():
    files = []

    if UPLOAD_DIR.exists():
        files = [f.name for f in UPLOAD_DIR.iterdir()]

    return {
        "path": str(UPLOAD_DIR),
        "exists": UPLOAD_DIR.exists(),
        "is_dir": UPLOAD_DIR.is_dir(),
        "files": files,
        "docs_count":len(files),
        "has_documents": len(files) > 0
    }