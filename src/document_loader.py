"""Модуль загрузки и обработки Markdown документов."""
from typing import List, Dict

from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_markdown_file(file_path: str) -> str:
    """
    Загружает содержимое Markdown файла.
    
    Args:
        file_path: Путь к .md файлу.
        
    Returns:
        Содержимое файла как строка.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def split_into_chunks(
    text: str,
    chunk_size: int = 500,
    chunk_overlap: int = 250,
) -> List[Dict]:
    """
    Разбивает текст на чанки для векторизации.
    
    Args:
        text: Исходный текст.
        chunk_size: Размер чанка в символах.
        chunk_overlap: Перекрытие между чанками.
        
    Returns:
        Список словарей с текстом и метаданными чанков.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n## ", "\n### ", "\n#### ", "\n\n", "\n", " ", ""],
    )
    
    chunk_texts = splitter.split_text(text)
    
    chunks = []
    for i, chunk_text in enumerate(chunk_texts):
        chunks.append({
            "text": chunk_text,
            "metadata": {
                "type": "markdown",
                "chunk_index": i,
            }
        })
    
    return chunks
