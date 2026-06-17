from app.services.llm_chain import ContractLLMChain


class QueryService:

    def __init__(self, llm_chain: ContractLLMChain):
        self.llm_chain = llm_chain

    async def ask_question(self, question: str):
        response = self.llm_chain.answer(
            question=question
        )

        return response