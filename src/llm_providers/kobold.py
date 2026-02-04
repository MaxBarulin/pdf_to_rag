"""KoboldCPP LLM провайдер через OpenAI-совместимый API."""
from typing import List, Dict

from openai import OpenAI

from .base import BaseLLMProvider


class KoboldProvider(BaseLLMProvider):
    """
    KoboldCPP провайдер.
    
    Использует OpenAI-совместимый API KoboldCPP.
    KoboldCPP должен быть запущен локально.
    """
    
    def __init__(self, base_url: str = "http://localhost:5001/v1"):
        """
        Инициализация KoboldCPP провайдера.
        
        Args:
            base_url: Базовый URL KoboldCPP API.
        """
        # KoboldCPP не требует API ключ
        self.client = OpenAI(base_url=base_url, api_key="not-needed")
        self.model = "koboldcpp"  # KoboldCPP игнорирует название модели
    
    def generate(self, messages: List[Dict[str, str]]) -> str:
        """
        Генерирует ответ через KoboldCPP API.
        
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
            return f"Ошибка при обращении к KoboldCPP: {e}"
