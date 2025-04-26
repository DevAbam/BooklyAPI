from fastapi import HTTPException, status
from sqlmodel import Session, select
from src.auth.schema import CreateUserModel
from src.auth.model import User
from src.auth.helpers import hash_user_password

class AuthService:
    def find_user_by_email(self, email, session):
        statement = select(User).where(User.email == email)
        return session.exec(statement).first()

    def check_user_exists(self, email:str, session:Session)-> bool:
        # statement = select(User).where(User.email == email)
        # user = session.exec(statement).first()
        user = self.find_user_by_email(email=email, session=session)
        return True if user is not None else False

    def create_user(self, user_data:CreateUserModel, session:Session): 
        user_data_dict = user_data.model_dump()
        user_password_str = user_data_dict.pop("password")
        user_data_dict["password"] = hash_user_password(user_password_str)
        new_user:User = User(**user_data_dict)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user


