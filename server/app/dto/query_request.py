from pydantic import BaseModel, Field
from typing import Optional


class QueryRequestDto(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        description="Natural language question about uploaded contracts"
    )