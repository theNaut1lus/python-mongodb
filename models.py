import uuid
from typing import Optional
from pydantic import BaseModel, Field


# base book model
class Book(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    author: str = Field(...)
    synopsis: str = Field(...)

    class Config:
        allow_population_by_field_name = True

        # example for schema in FASTAPI
        model_config = {
            "populate_by_name": True,
            "json_schema_extra": {
                "examples": [
                    {
                        "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                        "title": "Don Quixote",
                        "author": "Miguel de Cervantes",
                        "synopsis": "...",
                    }
                ]
            },
        }


# class to build query to update the book document
class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    synopsis: Optional[str]

    # example for schema in FASTAPI
    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "examples": [
                {
                    "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                    "title": "Don Quixote",
                    "author": "Miguel de Cervantes",
                    "synopsis": "...",
                }
            ]
        },
    }
