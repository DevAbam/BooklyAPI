from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id:Optional[UUID] = Field(default_factory=uuid4, primary_key=True, index=True)
    username:str
    email:str
    firstname:str
    lastname:str
    password:str
    created_at:datetime = Field(default_factory= datetime.now)
    updated_at:datetime = Field(default_factory= datetime.now)

    def __repr__(self):
        return f"<User : {self.username}>"
