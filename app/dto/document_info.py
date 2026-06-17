from datetime import datetime
from pydantic import BaseModel


class DocumentInfoDto(BaseModel):
    document_id: str
    filename: str
    uploaded_at: datetime
    chunk_count: int