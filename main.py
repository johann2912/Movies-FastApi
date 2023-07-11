from fastapi import FastAPI
from config.database import engine, Base
from fastapi.responses import HTMLResponse
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.auth import auth_router

app = FastAPI()
app.title = "Aplicación de peliculas con FastApi"
app.version = "0.0.1"
app.description = "Los servicios exponen informacion acerca de peliculas."

@app.get("/", tags=["home"])
def message():
    return HTMLResponse("<h1>Hello world!</h1>")


# middleware
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(auth_router)

# database connection
Base.metadata.create_all(bind=engine)