from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserModel(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    hash_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)