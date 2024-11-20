import json
from typing import List, Optional
from pathlib import Path


class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """Преобразует объект книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict) -> "Book":
        """Создает объект книги из словаря."""
        return Book(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"],
        )


class Library:
    def __init__(self, storage_file: str = "storage.json"):
        self.storage_file = Path(storage_file)
        if not self.storage_file.exists():
            self._initialize_storage()
        self.books: List[Book] = self._load_books()

    def _initialize_storage(self):
        """Инициализация пустого JSON-файла."""
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)

    def _load_books(self) -> List[Book]:
        """Загружает книги из JSON-файла."""
        with open(self.storage_file, "r", encoding="utf-8") as f:
            return [Book.from_dict(book) for book in json.load(f)]

    def _save_books(self):
        """Сохраняет книги в JSON-файл."""
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)
