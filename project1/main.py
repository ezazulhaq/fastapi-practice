from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/")
def get_books():
    """
        Get all the books
    """
    return BOOKS

@app.get("/books/{title}")
def get_book_by_title(title: str):
    """
        Get Books by Title
    """
    for book in BOOKS:
        if book.get('title').casefold() == title.casefold():
            return book

@app.get("/books/{author}/") 
def get_books_by_author_and_category(author: str, category: str):
    """
        Get Books by Author and Category
    """
    books = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books.append(book)
    return books

@app.post("/books/add")
def add_books(new_book=Body()):
    """
        Add New Book
    """
    BOOKS.append(new_book)