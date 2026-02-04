"""Базовый класс для LLM провайдеров."""
from abc import ABC, abstractmethod
from typing import List, Dict


class BaseLLMProvider(ABC):
    """Абстрактный базовый класс для LLM провайдеров."""
    
    @abstractmethod
    def generate(self, messages: List[Dict[str, str]]) -> str:
        """
        Генерирует ответ на основе сообщений.
        
        Args:
            messages: Список сообщений в формате [{"role": "user/assistant/system", "content": "..."}]
            
        Returns:
            Ответ модели.
        """
        pass
    
    def generate_with_context(self, query: str, context: str, system_prompt: str = None) -> str:
        """
        Генерирует ответ с учётом контекста из RAG.
        
        Args:
            query: Вопрос пользователя.
            context: Релевантный контекст из базы знаний.
            system_prompt: Системный промпт (опционально).
            
        Returns:
            Ответ модели.
        """
        if system_prompt is None:
            system_prompt = (
                "Ты — полезный ассистент. Отвечай на вопросы, используя предоставленный контекст. "
                "Если ответа нет в контексте, скажи об этом честно."
            )
        
        user_message = f"Контекст:\n{context}\n\nВопрос: {query}"
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ]
        
        return self.generate(messages)
