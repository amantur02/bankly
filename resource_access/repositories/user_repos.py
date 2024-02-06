from sqlalchemy import select
from sqlalchemy.orm import Session

from exceptions import NotFoundException
from resource_access.db_models.user_models import UserDB
from schemas.enums import UserRoleEnum
from schemas.user_schemas import User


class UserRepository:
    def __init__(self, db_session: Session):
        self._db_session = db_session

    async def get_client_user_by_phone_number(self, phone_number: str) -> User:
        query = await self._db_session.execute(
            select(UserDB).where(
                UserDB.phone == phone_number,
                UserDB.role == UserRoleEnum.client,
                UserDB.is_deleted.is_(False),
            )
        )
        user_db = query.scalar()
        if user_db:
            return User.model_validate(user_db)
        raise NotFoundException(
            f"There is no client with this phone number: {phone_number}"
        )

    async def get_user_by_email(self, email: str) -> User:
        query = await self._db_session.execute(
            select(UserDB).where(
                UserDB.email == email,
                UserDB.is_deleted.is_(False),
            )
        )
        user_db = query.scalar()
        if user_db:
            return User.model_validate(user_db)

