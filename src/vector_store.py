"""Модуль для работы с FAISS + BM25 гибридным поиском."""
import os
import pickle
from typing import List, Dict, Tuple
from collections import Counter
import math
import re

from langchain_community.vectorstores import FAISS

from .embeddings import QwenEmbeddings


class BM25:
    """
    BM25 алгоритм для ключевого поиска.
    
    BM25 находит документы по совпадению слов (как Google),
    в отличие от векторного поиска, который ищет по смыслу.
    """
    
    def __init__(self, documents: List[str], k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.documents = documents
        self.doc_count = len(documents)
        
        # Токенизация
        self.tokenized_docs = [self._tokenize(doc) for doc in documents]
        
        # Средняя длина документа
        self.avg_doc_len = sum(len(doc) for doc in self.tokenized_docs) / self.doc_count if self.doc_count > 0 else 0
        
        # IDF для каждого слова
        self.idf = self._calculate_idf()
    
    def _tokenize(self, text: str) -> List[str]:
        """Простая токенизация: разбивка на слова и нижний регистр."""
        # Разбиваем по пробелам и пунктуации
        words = re.findall(r'\b\w+\b', text.lower())
        return words
    
    def _calculate_idf(self) -> Dict[str, float]:
        """Вычисляет IDF (Inverse Document Frequency) для каждого слова."""
        word_doc_count = Counter()
        for doc in self.tokenized_docs:
            unique_words = set(doc)
            for word in unique_words:
                word_doc_count[word] += 1
        
        idf = {}
        for word, count in word_doc_count.items():
            idf[word] = math.log((self.doc_count - count + 0.5) / (count + 0.5) + 1)
        
        return idf
    
    def score(self, query: str, doc_idx: int) -> float:
        """Вычисляет BM25 score для документа."""
        query_tokens = self._tokenize(query)
        doc_tokens = self.tokenized_docs[doc_idx]
        doc_len = len(doc_tokens)
        
        word_counts = Counter(doc_tokens)
        
        score = 0.0
        for word in query_tokens:
            if word not in self.idf:
                continue
            
            freq = word_counts.get(word, 0)
            numerator = freq * (self.k1 + 1)
            denominator = freq + self.k1 * (1 - self.b + self.b * doc_len / self.avg_doc_len)
            score += self.idf[word] * numerator / denominator
        
        return score
    
    def search(self, query: str, k: int = 10) -> List[Tuple[int, float]]:
        """
        Поиск топ-k документов по BM25.
        
        Returns:
            Список кортежей (индекс документа, score).
        """
        scores = [(i, self.score(query, i)) for i in range(self.doc_count)]
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:k]


class HybridVectorStore:
    """
    Гибридное хранилище: FAISS (векторный) + BM25 (ключевой).
    
    Объединяет результаты обоих методов для лучшего качества поиска.
    """
    
    def __init__(
        self,
        embeddings: QwenEmbeddings,
        persist_directory: str = "./faiss_index",
    ):
        self.embeddings = embeddings
        self.persist_directory = os.path.abspath(persist_directory)
        self.faiss_store = None
        self.bm25 = None
        self.documents = []
    
    def add_documents(self, chunks: List[Dict]) -> None:
        """Добавляет документы в оба хранилища."""
        if not chunks:
            return
        
        texts = [chunk["text"] for chunk in chunks]
        metadatas = [chunk.get("metadata", {}) for chunk in chunks]
        self.documents = texts
        
        # Создаём FAISS индекс
        print(f"Создание FAISS индекса из {len(texts)} чанков...")
        self.faiss_store = FAISS.from_texts(texts, self.embeddings, metadatas=metadatas)
        
        # Создаём BM25 индекс
        print("Создание BM25 индекса...")
        self.bm25 = BM25(texts)
        
        # Сохраняем
        self._save()
    
    def _save(self) -> None:
        """Сохраняет индексы на диск."""
        os.makedirs(self.persist_directory, exist_ok=True)
        
        # Сохраняем FAISS
        self.faiss_store.save_local(self.persist_directory)
        
        # Сохраняем BM25 и документы
        bm25_path = os.path.join(self.persist_directory, "bm25.pkl")
        with open(bm25_path, "wb") as f:
            pickle.dump({"bm25": self.bm25, "documents": self.documents}, f)
        
        print(f"Индексы сохранены в '{self.persist_directory}'")
    
    def _load(self) -> bool:
        """Загружает индексы с диска. Возвращает True если успешно."""
        faiss_path = os.path.join(self.persist_directory, "index.faiss")
        bm25_path = os.path.join(self.persist_directory, "bm25.pkl")
        
        if not os.path.exists(faiss_path) or not os.path.exists(bm25_path):
            return False
        
        # Загружаем FAISS
        self.faiss_store = FAISS.load_local(
            self.persist_directory,
            self.embeddings,
            allow_dangerous_deserialization=True,
        )
        
        # Загружаем BM25
        with open(bm25_path, "rb") as f:
            data = pickle.load(f)
            self.bm25 = data["bm25"]
            self.documents = data["documents"]
        
        print(f"Загружено {len(self.documents)} документов из '{self.persist_directory}'")
        return True
    
    def similarity_search(
        self,
        query: str,
        k: int = 10,
        vector_weight: float = 0.5,
    ) -> List[Dict]:
        """
        Гибридный поиск: объединяет результаты FAISS и BM25.
        
        Args:
            query: Поисковый запрос.
            k: Количество результатов.
            vector_weight: Вес векторного поиска (0.0-1.0). BM25 weight = 1 - vector_weight.
            
        Returns:
            Список документов с текстом и комбинированным score.
        """
        bm25_weight = 1.0 - vector_weight
        
        # Получаем больше результатов для объединения
        fetch_k = min(k * 3, len(self.documents))
        
        # FAISS поиск
        faiss_results = self.faiss_store.similarity_search_with_score(query, k=fetch_k)
        
        # BM25 поиск
        bm25_results = self.bm25.search(query, k=fetch_k)
        
        # Нормализация и объединение scores
        scores = {}
        
        # Нормализуем FAISS scores (меньше = лучше, инвертируем)
        if faiss_results:
            max_faiss = max(score for _, score in faiss_results) or 1
            for doc, score in faiss_results:
                # Инвертируем: высокий score = хорошо
                normalized_score = 1 - (score / max_faiss) if max_faiss > 0 else 0
                text = doc.page_content
                scores[text] = scores.get(text, 0) + normalized_score * vector_weight
        
        # Нормализуем BM25 scores
        if bm25_results:
            max_bm25 = max(score for _, score in bm25_results) or 1
            for doc_idx, score in bm25_results:
                normalized_score = score / max_bm25 if max_bm25 > 0 else 0
                text = self.documents[doc_idx]
                scores[text] = scores.get(text, 0) + normalized_score * bm25_weight
        
        # Сортируем по комбинированному score
        sorted_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        # Форматируем результаты
        results = []
        for text, score in sorted_results[:k]:
            results.append({
                "text": text,
                "score": score,
            })
        
        return results
    
    def count(self) -> int:
        """Возвращает количество документов."""
        return len(self.documents)
    
    def is_empty(self) -> bool:
        """Проверяет, пусто ли хранилище."""
        return self.count() == 0


def get_or_create_vector_store(
    chunks: List[Dict],
    embeddings: QwenEmbeddings,
    persist_directory: str = "./faiss_index",
    force_recreate: bool = False,
) -> HybridVectorStore:
    """
    Загружает существующее или создаёт новое хранилище.
    """
    import shutil
    
    if force_recreate and os.path.exists(persist_directory):
        shutil.rmtree(persist_directory)
        print(f"Удалена старая база: {persist_directory}")
    
    store = HybridVectorStore(embeddings, persist_directory)
    
    # Пробуем загрузить
    if not force_recreate and store._load():
        return store
    
    # Если не загрузилось — создаём
    if chunks:
        print("Создание нового индекса...")
        store.add_documents(chunks)
    
    return store
