from typing import Dict
from uuid import uuid4

from sqlalchemy.orm import Session

from engines.auth_engines import AuthenticationEngine
from exceptions import AlreadyExistsException
from jwt_tokens import create_access_token, create_refresh_token
from resource_access.repositories.redis_repos import RedisRepository
from resource_access.repositories.user_repos import UserRepository
from schemas.auth_schemas import SMSRecord, AllowedTimeToResendCode
from schemas.user_schemas import Client


async def client_login_usecase(
        db_session: Session, phone_number: str, password: str
) -> Dict[str, str]:
    repo = UserRepository(db_session)
    user = await repo.get_client_user_by_phone_number(phone_number)
    await AuthenticationEngine.validate_password(user, password)

    return {
        "access_token": create_access_token(user_id=user.id),
        "refresh_token": create_refresh_token(user_id=user.id),
        "token_type": "bearer",
    }


async def send_verification_code_email_usecase(
        db_session: Session, sms_record: SMSRecord
):  # add successful message or time
    user_repo = UserRepository(db_session)
    engine = AuthenticationEngine()
    redis_repo = RedisRepository()

    if user_repo.get_user_by_email(sms_record.email):
        raise AlreadyExistsException("This email already exist")

    verification_code = str(uuid4().int)[:6]
    await engine.send_code_to_email(verification_code, sms_record.email)
    await redis_repo.set_verification_code(sms_record.email, verification_code)
