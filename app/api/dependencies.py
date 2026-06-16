
from app.services.document_processor import DocumentProcessor
from app.services.vector_store import VectorStoreService



def get_document_processor() -> DocumentProcessor:
    return DocumentProcessor()


def get_vector_store() -> VectorStoreService:
    return VectorStoreService()

