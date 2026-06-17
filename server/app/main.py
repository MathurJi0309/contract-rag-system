from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.db import connect_to_mongo, close_mongo
from app.core.middleware import cors_middlewares
from app.routes.index_route import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo()



app = FastAPI(
    title="AI Contract Analysis System",
    description="""
## AI-Powered Legal Contract Analysis

Upload legal/contract documents and ask questions grounded in their content.

### Features
- 📄 Upload multiple contract PDFs or text files
- 🔍 Semantic search using RAG (Retrieval-Augmented Generation)
- 💬 Natural language Q&A over your documents
- 🧠 Powered by LangChain + OpenAI + ChromaDB
    """,
    version="1.0.0",
    contact={
        "name": "Anilesh Mathur",
        "email": "dev.kg.mathurji@gmail.com",
    },
    lifespan=lifespan,
)

cors_middlewares(app)

app.include_router(api_router)