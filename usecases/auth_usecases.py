from typing import Dict

from sqlalchemy.orm import Session

from engines.auth_engines import AuthenticationEngine
from jwt_tokens import create_access_token, create_refresh_token
from resource_access.repositories.user_repos import UserRepository


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
