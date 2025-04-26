from fastapi import APIRouter,Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session
from src.db.db_config import get_session
from src.auth.schema import CreateUserModel,CreateUserResponseModel,LoginModel
from src.auth.service import AuthService
from .helpers import verify_password, create_access_token

auth_router = APIRouter()
auth_service = AuthService()

@auth_router.post("/signup", status_code=status.HTTP_200_OK, response_model=CreateUserResponseModel)
def create_user(user_data:CreateUserModel, session:Session = Depends(get_session)):
    user_exists = auth_service.check_user_exists(email=user_data.email, session=session)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User with email {user_data.email} already exists")
    new_user = auth_service.create_user(user_data,session)
    if new_user is not None:
        return new_user
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating user")

@auth_router.post("/login")
def login_user(user_data:LoginModel, session:Session = Depends(get_session)):
    user = auth_service.find_user_by_email(email=user_data.email, session=session)
    if user is not None:
        password_valid = verify_password(user_data.password, user.password)
        if password_valid:
            token = create_access_token(
                user_data={
                    "email":user.email,
                    "userId": str(user.id)
                }
            )
            return JSONResponse(
                content={
                    "message":"login successful",
                    "access-token":token,
                    "user":{
                        "email":user.email,
                        "uid":str(user.id)
                    }
                }
            )
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid credentials")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    
