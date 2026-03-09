from fastapi import APIRouter

from src.schemas.user import UserRead, UserUpdate
from src.auth.fastapi_users_router import fastapi_users
from src.config import settings

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)
