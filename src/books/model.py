from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

class BookModel(SQLModel, table= True):
    __tablename__ = "books"
    id:Optional[UUID] = Field(default_factory=uuid4, primary_key=True, index=True)
    title:str
    author:str
    page_count:int
    created_at:datetime = Field(default_factory=datetime.now)
    updated_at:datetime = Field(default_factory=datetime.now)

