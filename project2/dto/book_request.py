from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    id: int = Field(description="Unique Book ID", default=None)
    title: str = Field(min_length=2, max_length=15)
    author: str = Field(min_length=1, max_length=20)
    description: str = Field(min_length=5, max_length=25)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(min_digits=4, max_digits=4, le=2025, gt=1990)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Book Title",
                "author": "Book Author",
                "description": "Book Description",
                "rating": 4,
                "published_date": 2010
            }
        }
    }