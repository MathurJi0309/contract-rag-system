from typing import List, Optional

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document

from app.core.config import settings
from app.core.exceptions import NoDocumentsIngestedError
from app.services.vector_store import VectorStoreService
from app.dto.query_response import QueryResponseDto

SYSTEM_PROMPT = """You are a contract analysis assistant. Answer the user's question
ONLY using the contract excerpts provided in the context below.

Rules:
- If the answer is not present in the context, say clearly that the contract
  do not contain that information. Do NOT use outside/general knowledge.
- Quote or paraphrase the relevant clause where possible.
- If multiple documents are provided and they conflict, point out the conflict
  and name which document each part comes from.
- Be precise and concise. Avoid legal advice/opinions; state only what the
  document says.

Context:
{context}


"""

USER_PROMPT = "Question: {question}"


class ContractLLMChain:
    def __init__(self, vector_store: VectorStoreService):
        self.vector_store = vector_store
        self.llm = ChatOpenAI(
            model=settings.llm_model,
            temperature=0,
            api_key=settings.openai_api_key,
        )
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            ("user", USER_PROMPT),
        ])
        self.chain = self.prompt | self.llm | StrOutputParser()

    @staticmethod
    def create_context(chunks: List[Document]) -> str:
        context = ""
        for doc in chunks:
            context += doc.page_content + "\n\n"
        return context

    def answer(
        self,
        question: str
    ) -> QueryResponseDto:
        k =settings.retrieval_top_k
        retrieved = self.vector_store.similarity_search(question, k=k)

        if not retrieved:
            raise NoDocumentsIngestedError()

        context = self.create_context(retrieved)
        raw_answer = self.chain.invoke({"context": context, "question": question})


        return QueryResponseDto(
            question=question,
            answer=raw_answer.strip(),
           
        )
