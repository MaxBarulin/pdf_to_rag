"""RAG Chain — объединение поиска и генерации ответов."""
from typing import List, Dict

from .vector_store import HybridVectorStore
from .llm_providers.base import BaseLLMProvider


class RAGChain:
    """
    RAG (Retrieval-Augmented Generation) цепочка.
    
    Использует гибридный поиск (FAISS + BM25) для лучшего качества.
    """
    
    def __init__(
        self,
        vector_store: HybridVectorStore,
        llm_provider: BaseLLMProvider,
        top_k: int = 10,
        vector_weight: float = 0.5,
    ):
        """
        Инициализация RAG Chain.
        
        Args:
            vector_store: Гибридное хранилище.
            llm_provider: LLM провайдер для генерации ответов.
            top_k: Количество релевантных чанков для контекста.
            vector_weight: Вес векторного поиска (0.0-1.0).
        """
        self.vector_store = vector_store
        self.llm_provider = llm_provider
        self.top_k = top_k
        self.vector_weight = vector_weight
    
    def retrieve(self, query: str) -> List[Dict]:
        """
        Находит релевантные документы с помощью гибридного поиска.
        """
        return self.vector_store.similarity_search(
            query,
            k=self.top_k,
            vector_weight=self.vector_weight,
        )
    
    def generate(self, query: str) -> str:
        """
        Генерирует ответ на запрос с использованием RAG.
        """
        # Получаем релевантный контекст
        relevant_docs = self.retrieve(query)
        
        # Формируем контекст из найденных документов
        context_parts = []
        for i, doc in enumerate(relevant_docs, 1):
            text = doc["text"]
            score = doc.get("score", 0)
            context_parts.append(f"[Фрагмент {i}] (релевантность: {score:.2f})\n{text}")
        
        context = "\n\n---\n\n".join(context_parts)
        
        # Генерируем ответ через LLM
        return self.llm_provider.generate_with_context(query, context)
    
    def invoke(self, query: str) -> dict:
        """Совместимость с LangChain API."""
        result = self.generate(query)
        return {"result": result, "query": query}
