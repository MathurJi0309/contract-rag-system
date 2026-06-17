from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    openai_api_key: str

    mongo_uri: str = "mongodb://localhost:27017"
    mongo_db_name: str = "contract_qa"

    vector_store_dir: str = "./data/vectorstore"
    upload_dir: str = "./data/uploads"

    llm_model: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"
    chunk_size: int = 1000
    chunk_overlap: int = 150
    retrieval_top_k: int = 4
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int
    
    


settings = Settings()
