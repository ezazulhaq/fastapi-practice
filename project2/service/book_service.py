from project2.model.book import Book

class BookService:
    
    def fetch_id(self, book: Book, books: list[Book]) -> Book:
        book.id = 1 if len(books) == 0 else books[-1].id + 1
        return book