import os

import pdfplumber
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import RetrievalQA
import markdown


def wrap_text(text, max_length=80):
    """
    Разбивает текст на строки длиной не более max_length символов,
    добавляя перенос строки на месте ближайшего пробела.
    """
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        # Если добавление нового слова превышает лимит, завершаем текущую строку
        if sum(len(w) for w in current_line) + len(word) + len(current_line) > max_length:
            lines.append(' '.join(current_line))
            current_line = []
        current_line.append(word)

    # Добавляем оставшиеся слова
    if current_line:
        lines.append(' '.join(current_line))

    return '\n'.join(lines)


# === Шаг 1: Извлечение таблиц и текста из PDF ===
def extract_tables_as_dicts(pdf_path):
    tables_as_dicts = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()
            for table in tables:
                headers = table[0]  # Первая строка — заголовки
                rows = table[1:]  # Остальные строки — данные
                table_dict = [dict(zip(headers, row)) for row in rows]
                table_info = {
                    "page": page_number,
                    "table": table_dict
                }
                tables_as_dicts.append(table_info)

    return tables_as_dicts


def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Извлекаем текст, исключая области с таблицами
            tables = page.find_tables()
            non_table_text = page.filter(lambda obj: not any(obj.within_bbox(table.bbox) for table in tables))
            text += non_table_text.extract_text() or ""

    return text


# === Шаг 2: Объединение текста и таблиц ===
def combine_text_and_tables(text, tables_as_dicts):
    combined_data = []

    if text.strip():
        combined_data.append({"type": "text", "content": text})

    for table_info in tables_as_dicts:
        table_text = f"Table from page {table_info['page']}:\n"
        for row in table_info["table"]:
            table_text += ", ".join(f"{key}: {value}" for key, value in row.items()) + "\n"
        combined_data.append({"type": "table", "content": table_text})

    return combined_data


# === Шаг 3: Разделение на чанки ===
def split_into_chunks(combined_data, chunk_size=500, overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )

    chunks = []
    for item in combined_data:
        content = item["content"]
        metadata = {"type": item["type"]}

        chunk_texts = splitter.split_text(content)
        for chunk in chunk_texts:
            chunks.append({"text": chunk, "metadata": metadata})

    return chunks


# === Шаг 4: Создание и сохранение векторного хранилища ===
def create_and_save_vector_store(chunks, save_path="faiss_index"):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    texts = [chunk["text"] for chunk in chunks]
    metadatas = [chunk["metadata"] for chunk in chunks]

    vector_store = FAISS.from_texts(texts, embeddings, metadatas=metadatas)
    vector_store.save_local(save_path)
    print(f"Векторное хранилище сохранено в '{save_path}'")
    return vector_store


def load_vector_store(load_path="faiss_index"):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.load_local(
        load_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    print(f"Векторное хранилище загружено из '{load_path}'")
    return vector_store


# === Шаг 5: Настройка цепочки RAG ===
def setup_rag_chain(vector_store, api_key):
    llm = GoogleGenerativeAI(model="gemini-2.0-pro-exp-02-05", google_api_key=api_key)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )
    return qa_chain


# === Главная функция ===
def main(pdf_path, api_key):
    # Шаг 1: Извлечение данных из PDF
    tables_as_dicts = extract_tables_as_dicts(pdf_path)
    text = extract_text_from_pdf(pdf_path)

    # Шаг 2: Объединение текста и таблиц
    combined_data = combine_text_and_tables(text, tables_as_dicts)

    # Шаг 3: Разделение на чанки
    chunks = split_into_chunks(combined_data)

    # Шаг 4: Создание или загрузка векторного хранилища
    if not os.path.exists("faiss_index"):
        vector_store = create_and_save_vector_store(chunks)
    else:
        vector_store = load_vector_store()

    # Шаг 5: Настройка цепочки RAG
    qa_chain = setup_rag_chain(vector_store, api_key)

    # === Интерактивный чат ===
    print("\n=== Добро пожаловать в интерактивный чат! ===")
    print("Введите ваш вопрос или `/exit` для выхода.\n")

    while True:
        # Запрос от пользователя
        query = input("Вы: ")

        # Проверка на команду выхода
        if query.strip().lower() in ("/exit", "exit", "quit"):
            print("Система: До свидания!")
            break

        # Генерация ответа
        try:
            response = qa_chain.invoke(query)

            # Форматируем ответ
            if isinstance(response, dict) and "result" in response:
                result = response["result"]

                # Заменяем \n на реальные переносы строк
                result = result.replace("\\n", "\n")

                # Если нужно, преобразуем Markdown в HTML
                result = markdown.markdown(result)

                result = wrap_text(result, max_length=80)

                # Выводим только текстовый результат
                print(f"Система: {result}")
            else:
                print(f"Система: Не удалось получить ответ.")
        except Exception as e:
            print(f"Система: Произошла ошибка при обработке запроса: {e}")


# === Запуск программы ===
if __name__ == "__main__":
    # Загрузка переменных из .env
    load_dotenv()

    # Параметры
    pdf_path = os.getenv("PDF_PATH", "default_document.pdf")  # Путь к PDF
    api_key = os.getenv("GOOGLE_API_KEY")  # API-ключ для Google Gemini

    # Запуск
    main(pdf_path, api_key)