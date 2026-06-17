from fastapi import Depends
from app.services.document_processor import DocumentProcessor
from app.services.vector_store import VectorStoreService


def get_document_processor() -> DocumentProcessor:
    return DocumentProcessor()


def get_vector_store() -> VectorStoreService:
    return VectorStoreService()



from app.services.document_processor import DocumentProcessor
from app.services.vector_store import VectorStoreService

from .service import DocumentService
from .controller import DocumentController


def get_document_service(
    processor: DocumentProcessor = Depends(get_document_processor),
    vector_db: VectorStoreService = Depends(get_vector_store),
):
    return DocumentService(
        processor=processor,
        vector_db=vector_db,
    )


def get_document_controller(
    service: DocumentService = Depends(get_document_service),
):
    return DocumentController(service)