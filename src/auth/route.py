from fastapi import APIRouter,Depends, HTTPException, status
from sqlmodel import Session
from src.db.db_config import get_session
from src.auth.schema import CreateUserModel,CreateUserResponseModel
from src.auth.service import AuthService

auth_router = APIRouter()
auth_service = AuthService()

@auth_router.post("/signup", status_code=status.HTTP_200_OK, response_model=CreateUserResponseModel)
def create_user(user_data:CreateUserModel, session:Session = Depends(get_session)):
    new_user = auth_service.create_user(user_data,session)
    if new_user is not None:
        return new_user
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating user")