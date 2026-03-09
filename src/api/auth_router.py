from fastapi import APIRouter

from src.config import settings
from src.schemas.user import UserRead, UserCreate
from src.auth.backend import auth_backend
from src.auth.fastapi_users_router import fastapi_users

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

router.include_router(
    router=fastapi_users.get_auth_router(auth_backend),
)

router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate),
)

router.include_router(
    router=fastapi_users.get_verify_router(UserRead),
)

router.include_router(
    router=fastapi_users.get_reset_password_router(),
)
