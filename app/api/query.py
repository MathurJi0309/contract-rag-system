from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import get_llm_chain
from app.core.exceptions import BaseException
from app.dto.query_request import QueryRequestDto
from app.dto.query_response import QueryResponseDto
from app.services.llm_chain import ContractLLMChain

router = APIRouter(prefix="/query", tags=["query"])


@router.post("/", response_model=QueryResponseDto)
async def ask_question(
    request: QueryRequestDto,
    llm_chain: ContractLLMChain = Depends(get_llm_chain),
):
    """
    Answers a natural-language question grounded in the uploaded contract(s).
    Optionally scope to specific document_ids (e.g. when comparing two contracts).
    """
    try:
        response = llm_chain.answer(
            question=request.question,
        )

        # await queries_collection.insert_one({
        #     "question": request.question,
        #     "answer": response.answer,
        #     "document_ids": request.document_ids,
        #     "asked_at": datetime.now(timezone.utc),
        # })

        return response
    except BaseException as e:
        raise HTTPException(status_code=400, detail=str(e))
