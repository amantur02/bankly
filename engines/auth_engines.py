import requests
from passlib.context import CryptContext

from exceptions import AuthenticationError
from schemas.user_schemas import User

from core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthenticationEngine:
    @staticmethod
    async def validate_password(user: User, password: str):
        valid = False
        if user.hashed_password:
            valid = pwd_context.verify(password, user.hashed_password)
        if not valid:
            raise AuthenticationError(message="Incorrect password")

    @staticmethod
    async def send_code_to_email(code: str, email: str):
        params = {
            'format': 'json',
            'api_key': settings.UNI_API_KEY,
            'sender_name': settings.UNI_SENDER_NAME,
            'sender_email': settings.UNI_SENDER_EMAIL,
            'subject': "subject",
            'body': code,
            'list_id': email
        }

        response = requests.post(settings.UNI_URL, data=params)
        return response.json()

