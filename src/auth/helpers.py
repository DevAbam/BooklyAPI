from passlib.context import CryptContext
from dotenv import load_dotenv
import time
from uuid import uuid4
from typing import Optional
import os
import jwt
from jwt import PyJWTError
import logging

load_dotenv()
JWT_KEY=os.getenv('JWT_KEY')
JWT_ALGORITHM=os.getenv('JWT_ALGORITHM')
ACCESS_TOKEN_EXPIRY = 3600

password_encoder = CryptContext(
    schemes=["bcrypt"]
)
def hash_user_password(pwd:str):
    return password_encoder.hash(pwd)

def verify_password(pwd:str, hashedpassword):
    return password_encoder.verify(pwd, hashedpassword)

def create_access_token(user_data:dict, expiry:int=None , refresh:bool=False):
    payload = {
        "user": user_data,
        "exp": time.time() + (ACCESS_TOKEN_EXPIRY if expiry is None else expiry) ,
        "jti": str(uuid4()),
        "refresh":refresh
    }
    access_token =jwt.encode(
        algorithm=JWT_ALGORITHM,
        key=JWT_KEY,
        payload=payload
    )
    return access_token

def decode_access_token(token:str):
    try:
        token_data = jwt.decode(
            algorithms=JWT_ALGORITHM,
            key=JWT_KEY,
            jwt=token
        )
        return token_data
    except jwt.PyJWTError as e:
        logging.exception(e)
        return None








