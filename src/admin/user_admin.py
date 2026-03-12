from fastapi_users.password import PasswordHelper
from sqladmin import ModelView
from starlette.requests import Request

from src.models import UserOrm


password_helper = PasswordHelper()


class UserAdmin(ModelView, model=UserOrm):
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"

    column_exclude_list = ["hashed_password"]
    column_sortable_list = [
        "id",
        "email",
    ]

    async def on_model_change(
        self, data: dict, model: UserOrm, is_created: bool, request: Request
    ) -> None:
        raw_password = data.get("hashed_password") or password_helper.generate()
        if is_created or model.hashed_password != raw_password:
            data.update(hashed_password=password_helper.hash(raw_password))
