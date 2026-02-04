"""Модуль для работы с эмбеддингами Qwen3-Embedding-8B."""
import os
from typing import List

from langchain.embeddings.base import Embeddings
from sentence_transformers import SentenceTransformer


class QwenEmbeddings(Embeddings):
    """
    LangChain-совместимый класс для эмбеддингов Qwen3-Embedding-8B.
    
    При инициализации проверяет наличие модели локально.
    Если модель отсутствует — скачивает с HuggingFace.
    Оптимизирован для работы на CPU.
    """
    
    MODEL_NAME = "Qwen/Qwen3-Embedding-0.6B"
    
    def __init__(self, model_path: str = "./embedding_model"):
        """
        Инициализация эмбеддингов.
        
        Args:
            model_path: Путь для локального хранения модели.
        """
        self.model_path = os.path.abspath(model_path)
        self.model = self._load_model()
    
    def _load_model(self) -> SentenceTransformer:
        """Загружает модель локально или скачивает с HuggingFace."""
        
        # Проверяем, есть ли модель локально
        config_path = os.path.join(self.model_path, "config.json")
        
        if os.path.exists(config_path):
            print(f"Загрузка модели из локальной директории: {self.model_path}")
            model = SentenceTransformer(
                self.model_path,
                device="cpu",
                trust_remote_code=True,
            )
        else:
            print(f"Модель не найдена локально. Скачивание {self.MODEL_NAME}...")
            print("Это может занять несколько минут при первом запуске.")
            
            # Создаём директорию если её нет
            os.makedirs(self.model_path, exist_ok=True)
            
            # Загружаем модель с HuggingFace
            model = SentenceTransformer(
                self.MODEL_NAME,
                device="cpu",
                trust_remote_code=True,
            )
            
            # Сохраняем локально
            model.save(self.model_path)
            print(f"Модель сохранена в: {self.model_path}")
        
        return model
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Получает эмбеддинги для списка документов.
        
        Args:
            texts: Список текстов для эмбеддинга.
            
        Returns:
            Список эмбеддингов (векторов).
        """
        embeddings = self.model.encode(
            texts,
            show_progress_bar=True,
            convert_to_numpy=True,
        )
        return embeddings.tolist()
    
    def embed_query(self, text: str) -> List[float]:
        """
        Получает эмбеддинг для одного запроса.
        
        Args:
            text: Текст запроса.
            
        Returns:
            Эмбеддинг (вектор).
        """
        # Для запросов используем prompt_name="query" для лучшего качества поиска
        embedding = self.model.encode(
            text,
            prompt_name="query",
            convert_to_numpy=True,
        )
        return embedding.tolist()
