from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get(
    "/movies",
    tags=["movies"],
    response_model=List[Movie],
    status_code=200,
    dependencies=[Depends(JWTBearer())],
)
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()

    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get("/movies/{id}", tags=["movies"])
def get_movie(id: int = Path(ge=1, le=2000)):
    db = Session()
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Does not found"})

    return JSONResponse(content=jsonable_encoder(result))


@movie_router.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str = Query(min_length=5, max_length=120)):
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(
            status_code=404, content={"message": "Does not found category"}
        )

    return JSONResponse(content=jsonable_encoder(result))


@movie_router.post("/movies", tags=["movies"])
def create_movie(movie: Movie):
    db = Session()
    MovieService(db).create_movie(movie)

    return JSONResponse(content={"message": "successfully created"})


@movie_router.put("/movies/{id}", tags=["movies"])
def update_movie(id: int, movie: Movie):
    db = Session()
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Does not found"})
    MovieService(db).update_movie(id, movie)

    return JSONResponse(content={"message": "successfully changes"})


@movie_router.delete("/movies/{id}", tags=["movies"])
def delete_movie(id: int):
    db = Session()
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Does not found"})
    MovieService(db).delete_movie(id)

    return JSONResponse(content={"message": "successfully deleted"})
