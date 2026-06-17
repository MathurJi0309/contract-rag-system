from app.modules.users.service import UserService
from app.modules.users.dtos import (
    UserDTOSchema,
    LoginDTOSchema,
)

user_service = UserService()


class UserController:

    async def register_user(
        self,
        data: UserDTOSchema,
    ):
        return await user_service.register(
            data
        )

    async def login_user(
        self,
        data: LoginDTOSchema,
    ):
        return await user_service.login(
            data
        )



user_controller = UserController()