from fastapi import FastAPI

from project2.dto.book_request import BookRequest
from project2.model.book import Book
from project2.service.book_service import BookService

app = FastAPI()

BOOKS = [
    Book(1, "Title one", "Author one", "Description one", 5),
    Book(2, "Title two", "Author two", "Description two", 2),
    Book(3, "Title three", "Author three", "Description three", 1),
    Book(4, "Title four", "Author one", "Description four", 4),
    Book(5, "Title five", "Author three", "Description five", 3),
    Book(6, "Title six", "Author six", "Description six", 4),
]

@app.get("/books")
def get_book():
    """
        Get All Books
    """
    return BOOKS

@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    """
        Get Book By ID
    """
    for book in BOOKS:
        if book.id == book_id:
            return book
    return None

@app.get("/books/")
def get_books_by_rating(rating: int):
    """
        Get Books By Rating
    """
    books: list[Book] = []
    for book in BOOKS:
        if book.rating == rating:
            books.append(book)
    
    return books

@app.post("/book")
def add_book(book:BookRequest):
    """
        Add New Book
    """
    book_service = BookService()
    new_book = Book(**book.model_dump())
    BOOKS.append(book_service.fetch_id(new_book, BOOKS))
    return { "message": "Book Added Successfully"}

@app.put("/book/{book_id}")
def update_book_by_id(book_id: int, book: BookRequest):
    """
        Update Book By ID
    """
    for index, b in enumerate(BOOKS):
        if b.id == book_id:
            BOOKS[index] = Book(**book.model_dump())
            BOOKS[index].id = book_id
            return { "message": "Book Updated Successfully"}
    return { "message": "Book Not Found"}

@app.delete("/book/{book_id}")
def delete_book(book_id: int):
    """
        Delete Book By ID
    """
    for index, b in enumerate(BOOKS):
        if b.id == book_id:
            BOOKS.pop(index)
            return { "message": "Book Deleted Successfully"}
    return { "message": "Book Not Found"}