from resource_access.db_base_class import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ENUM

from schemas.enums import UserRoleEnum


class UserDB(Base):
    __tablename__ = "users"

    username = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    phone_number = Column(String(13))
    email = Column(String(200), nullable=True)
    role = Column(ENUM(UserRoleEnum, name="user_role_enum"))
    hashed_password = Column(String(300))
