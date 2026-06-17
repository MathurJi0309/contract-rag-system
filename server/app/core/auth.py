from fastapi import (
    Depends,
    HTTPException,
    status,
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

import jwt
from jwt.exceptions import InvalidTokenError

from app.core.config import settings
from app.modules.users.repository import UserRepository

security = HTTPBearer()

user_repository = UserRepository()


async def is_authenticated(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
):
    try:
        token = credentials.credentials

        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
        )

        user_id = payload.get("_id")

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized",
            )

        user = await user_repository.find_by_id(
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized",
            )

        user["id"] = str(user["_id"])
        del user["_id"]

        return user

    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )