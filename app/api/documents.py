from fastapi import APIRouter, status, UploadFile, File, Depends, HTTPException
from typing import List
from app.api.dependencies import get_document_processor, get_vector_store
from app.services.document_processor import DocumentProcessor
from app.core.exceptions import BaseException
from app.services.vector_store import VectorStoreService

router = APIRouter()


@router.post(
    "/upload",
    summary="Upload multiple contract documents",
    description="Upload multiple legal documents at once. All will be available for querying.",
    status_code=status.HTTP_201_CREATED,
)
async def upload_documents(
    files: List[UploadFile] = File(
        ..., description="Multiple contract files (PDF or TXT)"
    ),
    processor: DocumentProcessor = Depends(get_document_processor),
    vector_db: VectorStoreService = Depends(get_vector_store),
):
    try:
        if len(files) > 5:
            return HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Maximum 5 files per request.",
            )
        results = []
        for file in files:
            content = await file.read()
            stored_path, document_id = processor.save_upload(file.filename, content)
            chunks = processor.load_and_split(stored_path, document_id, file.filename)
            print("chunks", chunks)
            vector_db.add_documents(chunks)


            results.append(
                {
                    "document_id": document_id,
                    "filename": file.filename,
                    "chunks_indexed": len(chunks),
                }
            )

        return results
    except BaseException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
