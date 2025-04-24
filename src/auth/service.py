from fastapi import HTTPException, status
from sqlmodel import Session, select
from src.auth.schema import CreateUserModel
from src.auth.model import User
from src.auth.helpers import hash_user_password
class AuthService:
    def create_user(self, user_data:CreateUserModel, session:Session):
        #check if already exist then respond that they do
        check_statement = select(User).where(User.email == user_data.email)
        result = session.exec(check_statement).first()
        if result is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User with email {user_data.email} already exists")
        # go ahead and create the user
        user_data_dict = user_data.model_dump()
        user_password_str = user_data_dict.pop("password")
        user_data_dict["password"] = hash_user_password(user_password_str)
        new_user:User = User(**user_data_dict)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user


