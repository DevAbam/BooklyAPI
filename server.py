from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.db_config import initialize_db
from src.books.routes import books_router
from src.auth.route import auth_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("starting server")
    initialize_db()
    yield
    print("stopping server")

version = "v1"
app = FastAPI(lifespan=lifespan)
app.include_router(books_router, prefix=f"/api/{version}/books")
app.include_router(auth_router, prefix=f"/api/{version}/auth" )

