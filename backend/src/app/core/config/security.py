# security.py
from passlib.context import CryptContext
from settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def get_password_hash(plain: str) -> str:
    return pwd_context.hash(plain)
