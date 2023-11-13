from typing import Optional

from pydantic import BaseModel

from schemas.enums import UserRoleEnum


class User(BaseModel):
    id: Optional[int]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    role: Optional[UserRoleEnum]
    hashed_password: Optional[str]
    is_deleted: Optional[bool]

    class Config:
        orm_mode = True
