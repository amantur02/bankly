from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator
from pydantic.v1 import validator

from schemas.validators import validate_phone_number


class TokenPayload(BaseModel):
    sub: int


class ClientLoginIn(BaseModel):
    receiving_phone: str
    password: str

    _is_correct_phone_number = validator('receiving_phone', allow_reuse=True)(
        validate_phone_number
    )


class TokenSchema(BaseModel):
    access_token: Optional[str]
    refresh_token: Optional[str]
    token_type: Optional[str]


class ClientIn(BaseModel):
    username: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    password: str
    # _validate_password = validator("password", allow_reuse=True)(
    #     validate_password
    # )


class ClientOut(BaseModel):
    id: Optional[int]
    username: Optional[str]
    email: Optional[str]
    phone: Optional[str]


class AllowedTimeToResendCode(BaseModel):
    time: Optional[datetime]


class SendCodeEmailIn(BaseModel):
    email: str


class SMSRecord(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None

    class Config:
        from_attributes = True
