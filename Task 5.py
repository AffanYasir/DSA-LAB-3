def search_book(books, book_name):
    if book_name in books:
        print(f"Book '{book_name}' found in the library.")
    else:
        print(f"Book '{book_name}' not found.")


books = ["Book1", "Book2", "Book3"]
search_book(books, "Book2")