from fastapi_users import FastAPIUsers

from src.auth.backend import auth_backend
from src.dependencies.auth.user_manager import get_user_manager
from src.models.user import UserOrm

fastapi_users = FastAPIUsers[UserOrm, int](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)