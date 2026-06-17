from fastapi import HTTPException, status
from app.core.exceptions import BaseException
from .service import DocumentService


class DocumentController:

    def __init__(self, service: DocumentService):
        self.service = service

    async def upload_documents(self, files):
        try:
            return await self.service.upload_documents(files)

        except BaseException as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e),
            )