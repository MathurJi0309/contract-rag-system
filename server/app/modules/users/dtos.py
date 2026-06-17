from pydantic import BaseModel


class UserDTOSchema(BaseModel):
    name: str
    password: str
    email: str


class UserResponseDTOSchema(BaseModel):
    name: str
    email: str
    id: str


class LoginDTOSchema(BaseModel):
    email: str
    password: str