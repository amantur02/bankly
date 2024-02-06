import json

from core.constants import VERIFICATION_CODE_KEY, VERIFICATION_CODE_EXPIRATION_SECONDS
from core.redis import redis_client


class RedisRepository:
    def __init__(self):
        self.redis = redis_client
        self.verification_code_key = VERIFICATION_CODE_KEY
        self.vc_expiration_seconds = VERIFICATION_CODE_EXPIRATION_SECONDS

    async def set_verification_code(self, email: str, code: str) -> None:
        await self.redis.set(
            self.verification_code_key.format(email=email),
            json.dumps({'code': code}),
            ex=self.vc_expiration_seconds,
        )
