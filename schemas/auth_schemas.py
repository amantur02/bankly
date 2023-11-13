from typing import Optional

from pydantic import BaseModel
from pydantic.v1 import validator

from schemas.validators import validate_phone_number


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
