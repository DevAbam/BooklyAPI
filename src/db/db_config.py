from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(url=DATABASE_URL, echo=True)

def initialize_db():
    try:
        from src.books.model import BookModel
        SQLModel.metadata.create_all(engine)
    except Exception as e:
        print(f"Error initializing database:  {e}")

def get_session():
    with Session(engine) as session:
        yield session
