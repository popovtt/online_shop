import asyncio
import contextlib
import logging
from os import getenv

from fastapi_users.exceptions import UserAlreadyExists

from src.models.user import UserOrm
from src.auth.user_manager import UserManager
from src.schemas.user import UserCreate
from src.dependencies.auth import get_user_manager
from src.dependencies.auth import get_user_db
from src.utils.db_helper import db_helper

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

default_email = getenv("DEFAULT_EMAIL", "admin@admin.com")
default_password = getenv("DEFAULT_PASSWORD", "abc")
default_is_active = True
default_is_superuser = True
default_is_verified = True


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> UserOrm:
    try:
        user = await user_manager.create(
            user_create=user_create,
            safe=False,
        )

    except UserAlreadyExists:
        log.info("User %r already exists", user_create.email)
        raise

    return user


async def create_superuser(
    email: str = default_email,
    password: str = default_password,
    is_active: bool = default_is_active,
    is_superuser: bool = default_is_superuser,
    is_verified: bool = default_is_verified,
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    async with db_helper.session_factory() as session:
        async with get_user_db_context(session) as users_db:
            async with get_user_manager_context(users_db) as user_manager:
                try:
                    user = await create_user(
                        user_manager=user_manager,
                        user_create=user_create,
                    )
                    log.info("Superuser created: %s", email)
                except UserAlreadyExists:
                    log.info("Superuser %s already exists", email)
                    user = await user_manager.user_db.get_by_email(
                        email
                    )  # Fetch existing user

                return user


if __name__ == "__main__":
    asyncio.run(create_superuser())
