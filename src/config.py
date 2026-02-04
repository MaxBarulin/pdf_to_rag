"""Конфигурация приложения."""
import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class Config:
    """Конфигурация приложения."""
    
    # LLM Provider: "polza" или "kobold"
    llm_provider: str
    
    # PolzaAI
    polza_api_key: str
    polza_base_url: str
    polza_model: str
    
    # KoboldCPP
    kobold_base_url: str
    
    # Документ
    document_path: str
    
    # Путь к модели эмбеддингов
    embedding_model_path: str
    
    # FAISS индекс
    faiss_index_path: str


def load_config() -> Config:
    """Загружает конфигурацию из .env файла."""
    load_dotenv()
    
    return Config(
        llm_provider=os.getenv("LLM_PROVIDER", "polza"),
        polza_api_key=os.getenv("POLZA_AI_API_KEY", ""),
        polza_base_url=os.getenv("POLZA_AI_BASE_URL", "https://polza.ai/api/v1"),
        polza_model=os.getenv("POLZA_AI_MODEL", "z-ai/glm-4.7-flash"),
        kobold_base_url=os.getenv("KOBOLD_BASE_URL", "http://localhost:5001/v1"),
        document_path=os.getenv("DOCUMENT_PATH", "Developers_Toolkit.md"),
        embedding_model_path=os.getenv("EMBEDDING_MODEL_PATH", "./embedding_model"),
        faiss_index_path=os.getenv("FAISS_INDEX_PATH", "./faiss_index"),
    )
