from pydantic import BaseModel


class DocumentUploadResponseDto(BaseModel):
    document_id: str
    filename: str
    chunks_indexed: int
    status: str = "processed"