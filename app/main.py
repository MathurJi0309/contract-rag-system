from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import documents,query
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
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {
        "status": "running",
        "message": "AI Contract Analysis System is live",
        "docs": "/docs",
    }


app.include_router(documents.router,prefix="/api/v1/documents")
app.include_router(query.router,prefix="/api/v1/query")