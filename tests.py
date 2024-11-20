import unittest
from handlers import LibraryManager


class TestLibraryManager(unittest.TestCase):
    def setUp(self):
        self.manager = LibraryManager()

    def test_add_book(self):
        initial_count = len(self.manager.library.books)
        self.manager.add_book("Test Book", "Test Author", 2024)
        self.assertEqual(len(self.manager.library.books), initial_count + 1)

    def test_remove_book(self):
        self.manager.add_book("To Remove", "Author", 2024)
        book_id = self.manager.library.books[-1].id
        self.manager.remove_book(book_id)
        self.assertFalse(any(book.id == book_id for book in self.manager.library.books))

    def test_search_books(self):
        self.manager.add_book("Search Test", "Search Author", 2024)
        results = self.manager.search_books(title="Search")
        self.assertTrue(len(results) > 0)

    def test_update_status(self):
        self.manager.add_book("Status Test", "Author", 2024)
        book_id = self.manager.library.books[-1].id
        self.manager.update_status(book_id, "выдана")
        self.assertEqual(self.manager.library.books[-1].status, "выдана")


if __name__ == "__main__":
    unittest.main()
