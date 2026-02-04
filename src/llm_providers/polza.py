"""PolzaAI LLM провайдер через OpenAI-совместимый API."""
from typing import List, Dict

from openai import OpenAI

from .base import BaseLLMProvider


class PolzaProvider(BaseLLMProvider):
    """
    PolzaAI провайдер.
    
    Использует OpenAI-совместимый API polza.ai.
    """
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://polza.ai/api/v1",
        model: str = "z-ai/glm-4.7-flash",
    ):
        """
        Инициализация PolzaAI провайдера.
        
        Args:
            api_key: API ключ PolzaAI.
            base_url: Базовый URL API.
            model: Название модели.
        """
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = model
    
    def generate(self, messages: List[Dict[str, str]]) -> str:
        """
        Генерирует ответ через PolzaAI API.
        
        Args:
            messages: Список сообщений.
            
        Returns:
            Ответ модели.
        """
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Ошибка при обращении к PolzaAI: {e}"
