from fastapi import Depends
from app.services.llm_chain import ContractLLMChain
from .service import QueryService
from .controller import QueryController
from app.services.llm_chain import ContractLLMChain 
from app.services.vector_store import VectorStoreService

def get_vector_store() -> VectorStoreService:
    return VectorStoreService()
def get_llm_chain() -> ContractLLMChain:
    return ContractLLMChain(vector_store=get_vector_store())

def get_query_service(
    llm_chain: ContractLLMChain = Depends(get_llm_chain),
):
    return QueryService(
        llm_chain=llm_chain
    )


def get_query_controller(
    service: QueryService = Depends(get_query_service),
):
    return QueryController(service)