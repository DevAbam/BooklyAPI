from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel

class Book(BaseModel):
    id:UUID 
    title:str
    author:str
    page_count:int
    created_at:datetime
    updated_at:datetime
 
class BookResponse(BaseModel):
    data: Book

class AllBookResponse(BaseModel):
    data: List[Book]

class BookCreateModel(BaseModel):
    title:str
    author:str
    page_count:int

class BookUpdateModel(BaseModel):
    title:str
    author:str
    page_count:int