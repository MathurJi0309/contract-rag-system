from fastapi import APIRouter, Request, status

from app.modules.users.dtos import (
    UserDTOSchema,
    UserResponseDTOSchema,
    LoginDTOSchema,
)

from app.modules.users.controller import UserController


UserController=UserController()

user_router = APIRouter(

)


@user_router.post(
    "/register",
    response_model=UserResponseDTOSchema,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    body: UserDTOSchema,
):
    return await UserController.register_user(body)


@user_router.post(
    "/login",
    status_code=status.HTTP_200_OK,
)
async def login(
    body: LoginDTOSchema,
):
    return await UserController.login_user(body)

