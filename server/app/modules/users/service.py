from app.modules.users.repository import UserRepository
from pwdlib import PasswordHash

from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, status

from app.core.config import settings


user_repository = UserRepository()
password_hash = PasswordHash.recommended()
def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password):
    return password_hash.hash(password)

class UserService:

    async def register(self, data):
        # validation
        # password hashing
        # business logic

        existing_user = (
            await user_repository.find_by_email(
                data.email
            )
        )

        if existing_user:
            raise Exception(
                "User already exists"
            )
        user_data = {
            "name": data.name,
            "email": data.email,
            "hash_password": get_password_hash(
                data.password
            ),
        }

        user_id = await user_repository.create_user(
            user_data
        )


        return {
        "id": str(user_id),
        "name": data.name,
        "email": data.email,
        }



    async def login(self, data):
        user = await user_repository.find_by_email(
            data.email
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        is_valid = verify_password(
            data.password,
            user["hash_password"],
        )

        if not is_valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        exp_time = datetime.utcnow() + timedelta(
            minutes=settings.access_token_expire_minutes
        )

        token = jwt.encode(
            {
                "_id": str(user["_id"]),
                "email": user["email"],
                "exp": exp_time,
            },
            settings.secret_key,
            algorithm=settings.algorithm,
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "id": str(user["_id"]),
                "name": user["name"],
                "email": user["email"],
            },
        }
        

