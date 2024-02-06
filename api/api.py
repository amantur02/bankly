from fastapi import APIRouter
from api.customer import auth_endpoints as auth_router

api_router = APIRouter()

api_router.include_router(
    auth_router.router, prefix="/auth", tags=["authentication"]
)
