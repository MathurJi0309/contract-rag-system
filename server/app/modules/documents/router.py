from typing import List

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    status,
)

from app.core.auth import is_authenticated

from .controller import DocumentController
from .dependencies import get_document_controller

router = APIRouter()


@router.post(
    "/upload",
    summary="Upload multiple contract documents",
    description="Upload multiple legal documents at once. All will be available for querying.",
    status_code=status.HTTP_201_CREATED,
)
async def upload_documents(
    files: List[UploadFile] = File(
        ...,
        description="Multiple contract files (PDF or TXT)"
    ),
    controller: DocumentController = Depends(
        get_document_controller
    ),
    current_user=Depends(is_authenticated),
):
    return await controller.upload_documents(files)