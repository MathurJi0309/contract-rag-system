from fastapi import HTTPException

from app.core.exceptions import BaseException
from .service import QueryService


class QueryController:

    def __init__(self, service: QueryService):
        self.service = service

    async def ask_question(self, question: str):
        try:
            return await self.service.ask_question(question)

        except BaseException as e:
            raise HTTPException(
                status_code=400,
                detail=str(e)
            )