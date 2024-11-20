from models import Library, Book
from typing import Optional


class LibraryManager:
    def __init__(self):
        self.library = Library()

    def add_book(self, title: str, author: str, year: int):
        """Добавляет книгу в библиотеку."""
        new_id = max([book.id for book in self.library.books], default=0) + 1
        new_book = Book(id=new_id, title=title, author=author, year=year)
        self.library.books.append(new_book)
        self.library._save_books()

    def remove_book(self, book_id: int):
        """Удаляет книгу по ID."""
        self.library.books = [book for book in self.library.books if book.id != book_id]
        self.library._save_books()

    def search_books(self, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None):
        """Ищет книги по title, author или year."""
        result = self.library.books
        if title:
            result = [book for book in result if title.lower() in book.title.lower()]
        if author:
            result = [book for book in result if author.lower() in book.author.lower()]
        if year:
            result = [book for book in result if book.year == year]
        return result

    def list_books(self):
        """Возвращает список всех книг."""
        return self.library.books

    def update_status(self, book_id: int, status: str):
        """Обновляет статус книги."""
        for book in self.library.books:
            if book.id == book_id:
                book.status = status
        self.library._save_books()
