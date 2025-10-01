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

@app.post("/book")
def add_book(book:BookRequest):
    """
        Add New Book
    """
    book_service = BookService()
    new_book = Book(**book.model_dump())
    BOOKS.append(book_service.fetch_id(new_book, BOOKS))
    return { "message": "Book Added Successfully"}