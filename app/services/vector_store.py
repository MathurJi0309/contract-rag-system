from typing import List, Optional

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

from app.core.config import settings



class VectorStoreService:
    """
    here we do two things store in vector db and similarity search.
    """

    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            model=settings.embedding_model,
            api_key=settings.openai_api_key,
            
        )
        self.store = Chroma(
            collection_name="contracts",
            embedding_function=self.embeddings,
            persist_directory=settings.vector_store_dir,
        )

    def add_documents(self, chunks: List[Document]) -> None:
        if chunks:
            self.store.add_documents(chunks)

  