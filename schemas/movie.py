from pydantic import BaseModel, Field
from typing import Optional, List


class Movie(BaseModel):
    title: str = Field(min_length=3, max_length=15)
    overview: str
    year: int = Field(ge=1, le=2023)
    category: str
    rating: float

    class Config:
        schema_extra = {
            "example": {
                "title": "Titulo de mi pelicula",
                "overview": "Descipcion pelicula",
                "year": 2023,
                "category": "Categoria de mi pelicula",
                "rating": 9.5,
            }
        }
