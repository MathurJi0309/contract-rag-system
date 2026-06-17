
from app.services.document_processor import DocumentProcessor
from app.services.vector_store import VectorStoreService
from app.services.llm_chain import ContractLLMChain 


def get_document_processor() -> DocumentProcessor:
    return DocumentProcessor()


def get_vector_store() -> VectorStoreService:
    return VectorStoreService()

def get_llm_chain() -> ContractLLMChain:
    return ContractLLMChain(vector_store=get_vector_store())
