from handlers import LibraryManager

manager = LibraryManager()

def main_menu():
    print("\nУправление библиотекой:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Искать книгу")
    print("4. Показать все книги")
    print("5. Изменить статус книги")
    print("0. Выход")

def run():
    while True:
        main_menu()
        choice = input("Введите команду: ").strip()

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            manager.add_book(title, author, year)
            print("Книга успешно добавлена!")
        
        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            manager.remove_book(book_id)
            print("Книга успешно удалена!")

        elif choice == "3":
            title = input("Введите название книги (или оставьте пустым): ")
            author = input("Введите автора книги (или оставьте пустым): ")
            year = input("Введите год издания (или оставьте пустым): ")
            year = int(year) if year else None
            results = manager.search_books(title=title, author=author, year=year)
            if results:
                for book in results:
                    print(f"{book.id}: {book.title} - {book.author} ({book.year}) [{book.status}]")
            else:
                print("Книг не найдено.")

        elif choice == "4":
            books = manager.list_books()
            for book in books:
                print(f"{book.id}: {book.title} - {book.author} ({book.year}) [{book.status}]")
        
        elif choice == "5":
            book_id = int(input("Введите ID книги: "))
            status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            manager.update_status(book_id, status)
            print("Статус книги успешно обновлен!")
        
        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Некорректная команда. Попробуйте снова.")


if __name__ == "__main__":
    run()
