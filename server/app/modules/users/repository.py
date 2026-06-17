from app.core.db import mongodb
from bson import ObjectId
from app.modules.users.models import UserModel


class UserRepository:

    @property
    def collection(self):
        return mongodb.database.users

    async def create_user(self, user: UserModel):
        result = await self.collection.insert_one(
            user
        )

        print('result',result.inserted_id)

        return result.inserted_id

    async def find_by_email(self, email: str):
        return await self.collection.find_one(
            {"email": email}
        )
    
    async def find_by_id(self, user_id: str):
        return await self.collection.find_one(
            {
                "_id": ObjectId(user_id)
            }
        )