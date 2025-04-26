from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class CreateUserModel(BaseModel):
    username:str = Field(min_length=3, max_length=22)
    email:str 
    firstname:str
    lastname:str
    password:str = Field(min_length=4, max_length=10)

class CreateUserResponseModel(BaseModel):
    id:UUID
    username:str
    email:str
    firstname:str
    lastname:str
    created_at:datetime 
    updated_at:datetime  

class LoginModel(BaseModel):
    email:str
    password:str
