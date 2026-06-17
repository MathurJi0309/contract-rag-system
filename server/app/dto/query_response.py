from typing import List, Optional
from pydantic import BaseModel


class QueryResponseDto(BaseModel):
    question: str
    answer: str
