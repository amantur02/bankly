from passlib.context import CryptContext

from exceptions import AuthenticationError
from schemas.user_schemas import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthenticationEngine:
    @staticmethod
    async def validate_password(user: User, password: str):
        valid = False
        if user.hashed_password:
            valid = pwd_context.verify(password, user.hashed_password)
        if not valid:
            raise AuthenticationError(message="Incorrect password")
