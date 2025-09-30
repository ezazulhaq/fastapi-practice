from fastapi import FastAPI

from project2.model.book import Book

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