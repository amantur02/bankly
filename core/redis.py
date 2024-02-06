import aioredis
from core.config import settings

redis_client = aioredis.from_url(
    f'redis://{settings.redis_host}:{settings.redis_port}',
    encoding="utf-8",
    decode_responses=True,
)
