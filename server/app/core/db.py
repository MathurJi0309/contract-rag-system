from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings


class MongoDB:
    client: AsyncIOMotorClient = None
    database = None


mongodb = MongoDB()


async def connect_to_mongo():
    mongodb.client = AsyncIOMotorClient(settings.mongo_uri)
    mongodb.database = mongodb.client[settings.mongo_db_name]

    print("✅ MongoDB Connected")


async def close_mongo():
    if mongodb.client:
        mongodb.client.close()
        print("❌ MongoDB Connection Closed")