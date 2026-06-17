from fastapi import APIRouter, Depends

from app.core.auth import is_authenticated

from app.dto.query_request import QueryRequestDto
from app.dto.query_response import QueryResponseDto

from .controller import QueryController
from .dependencies import get_query_controller

router = APIRouter(
    prefix="/query",
)


@router.post(
    "/",
    response_model=QueryResponseDto
)
async def ask_question(
    request: QueryRequestDto,
    controller: QueryController = Depends(
        get_query_controller
    ),
    current_user=Depends(is_authenticated)
):
    return await controller.ask_question(
        request.question
    )