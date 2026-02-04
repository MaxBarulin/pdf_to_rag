"""
RAG-система с гибридным поиском (FAISS + BM25).

Использует:
- Эмбеддинги: Qwen3-Embedding-0.6B (локально)
- Поиск: Гибридный (векторный + ключевой)
- LLM: PolzaAI или KoboldCPP
"""
import sys

from src.config import load_config
from src.embeddings import QwenEmbeddings
from src.document_loader import load_markdown_file, split_into_chunks
from src.vector_store import get_or_create_vector_store
from src.rag_chain import RAGChain
from src.llm_providers.polza import PolzaProvider
from src.llm_providers.kobold import KoboldProvider


def create_llm_provider(config):
    """Создаёт LLM провайдер на основе конфигурации."""
    if config.llm_provider == "kobold":
        print(f"Используем KoboldCPP: {config.kobold_base_url}")
        return KoboldProvider(base_url=config.kobold_base_url)
    else:
        print(f"Используем PolzaAI: {config.polza_model}")
        return PolzaProvider(
            api_key=config.polza_api_key,
            base_url=config.polza_base_url,
            model=config.polza_model,
        )


def wrap_text(text: str, max_length: int = 100) -> str:
    """Разбивает текст на строки."""
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        if sum(len(w) for w in current_line) + len(word) + len(current_line) > max_length:
            lines.append(' '.join(current_line))
            current_line = []
        current_line.append(word)

    if current_line:
        lines.append(' '.join(current_line))

    return '\n'.join(lines)


def main():
    """Главная функция приложения."""
    config = load_config()
    
    print("=" * 60)
    print("RAG-система с гибридным поиском (FAISS + BM25)")
    print("=" * 60)
    
    # Шаг 1: Инициализация эмбеддингов
    print("\n[1/4] Загрузка модели эмбеддингов...")
    embeddings = QwenEmbeddings(model_path=config.embedding_model_path)
    
    # Шаг 2: Загрузка документа
    print(f"\n[2/4] Загрузка документа: {config.document_path}")
    try:
        text = load_markdown_file(config.document_path)
        chunks = split_into_chunks(text)
        print(f"Документ разбит на {len(chunks)} чанков")
    except FileNotFoundError:
        print(f"Ошибка: Файл {config.document_path} не найден!")
        sys.exit(1)
    
    # Шаг 3: Создание/загрузка гибридного хранилища
    print(f"\n[3/4] Подготовка гибридного индекса (FAISS + BM25)...")
    vector_store = get_or_create_vector_store(
        chunks=chunks,
        embeddings=embeddings,
        persist_directory="./faiss_index",
    )
    
    # Шаг 4: Настройка LLM провайдера
    print(f"\n[4/4] Инициализация LLM провайдера...")
    llm_provider = create_llm_provider(config)
    
    # Создаём RAG Chain с настраиваемыми параметрами
    rag_chain = RAGChain(
        vector_store=vector_store,
        llm_provider=llm_provider,
        top_k=10,
        vector_weight=0.5,  # 50% вектор, 50% BM25
    )
    
    # Интерактивный чат
    print("\n" + "=" * 60)
    print("Добро пожаловать! Гибридный поиск активен.")
    print("Команды:")
    print("  /exit     — выход")
    print("  /reindex  — пересоздать индекс")
    print("  /bm25     — только BM25 (ключевой поиск)")
    print("  /vector   — только векторный поиск")
    print("  /hybrid   — гибридный поиск (по умолчанию)")
    print("=" * 60 + "\n")
    
    current_mode = "hybrid"
    
    while True:
        try:
            query = input(f"[{current_mode}] Вы: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nДо свидания!")
            break
        
        if not query:
            continue
        
        if query.lower() in ("/exit", "exit", "quit"):
            print("До свидания!")
            break
        
        if query.lower() == "/reindex":
            print("Пересоздание индекса...")
            vector_store = get_or_create_vector_store(
                chunks=chunks,
                embeddings=embeddings,
                persist_directory="./faiss_index",
                force_recreate=True,
            )
            rag_chain = RAGChain(
                vector_store=vector_store,
                llm_provider=llm_provider,
                top_k=10,
                vector_weight=0.5 if current_mode == "hybrid" else (1.0 if current_mode == "vector" else 0.0),
            )
            print("Индекс пересоздан!\n")
            continue
        
        if query.lower() == "/bm25":
            current_mode = "bm25"
            rag_chain.vector_weight = 0.0  # Только BM25
            print("Режим: только BM25 (ключевой поиск)\n")
            continue
        
        if query.lower() == "/vector":
            current_mode = "vector"
            rag_chain.vector_weight = 1.0  # Только векторный
            print("Режим: только векторный поиск\n")
            continue
        
        if query.lower() == "/hybrid":
            current_mode = "hybrid"
            rag_chain.vector_weight = 0.5  # Гибрид
            print("Режим: гибридный поиск (50/50)\n")
            continue
        
        try:
            response = rag_chain.invoke(query)
            result = response.get("result", "Не удалось получить ответ.")
            result = wrap_text(result)
            print(f"\nСистема: {result}\n")
        except Exception as e:
            print(f"\nОшибка: {e}\n")


if __name__ == "__main__":
    main()