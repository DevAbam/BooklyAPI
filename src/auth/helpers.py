from passlib.context import CryptContext

password_encoder = CryptContext(
    schemes=["bcrypt"]
)
def hash_user_password(pwd:str):
    return password_encoder.hash(pwd)


