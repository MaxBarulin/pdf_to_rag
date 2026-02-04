# RAG-система с Qwen3-Embedding-8B

Retrieval-Augmented Generation (RAG) система для работы с Markdown-документами.

## Возможности

- **Эмбеддинги**: Qwen3-Embedding-8B (локальная модель, CPU)
- **LLM провайдеры**: 
  - PolzaAI (облачный, OpenAI-совместимый API)
  - KoboldCPP (локальный)
- **Векторное хранилище**: FAISS
- **Документы**: Markdown (.md)

## Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/MaxBarulin/pdf_to_rag.git
cd pdf_to_rag
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка

Создайте файл `.env` (пример в `.env.example`):

```env
# LLM Provider: polza или kobold
LLM_PROVIDER=polza

# PolzaAI
POLZA_AI_API_KEY=ваш_ключ
POLZA_AI_BASE_URL=https://polza.ai/api/v1
POLZA_AI_MODEL=z-ai/glm-4.7-flash

# KoboldCPP (опционально)
KOBOLD_BASE_URL=http://localhost:5001/v1

# Документ
DOCUMENT_PATH=Developers_Toolkit.md

# Пути
EMBEDDING_MODEL_PATH=./embedding_model
FAISS_INDEX_PATH=./faiss_index
```

## Использование

```bash
python main.py
```

При первом запуске модель эмбеддингов (~16GB) будет автоматически скачана в `./embedding_model`.

### Переключение LLM провайдера

В `.env`:
- `LLM_PROVIDER=polza` — использовать PolzaAI (облако)
- `LLM_PROVIDER=kobold` — использовать KoboldCPP (локально)

Для KoboldCPP необходимо предварительно запустить сервер.

## Структура проекта

```
pdf_to_rag/
├── src/
│   ├── config.py            # Конфигурация
│   ├── embeddings.py        # Qwen3-Embedding-8B
│   ├── document_loader.py   # Загрузка .md файлов
│   ├── vector_store.py      # FAISS
│   ├── rag_chain.py         # RAG pipeline
│   └── llm_providers/
│       ├── base.py          # Базовый класс
│       ├── polza.py         # PolzaAI
│       └── kobold.py        # KoboldCPP
├── embedding_model/         # Локальная модель (создаётся автоматически)
├── faiss_index/             # Векторный индекс
├── main.py                  # Точка входа
├── requirements.txt
└── README.md
```

## Требования

- Python 3.8+
- ~16GB свободного места (для модели эмбеддингов)
- Рекомендуется: 32GB RAM для CPU-инференса 8B модели
