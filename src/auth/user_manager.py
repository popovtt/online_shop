import logging
from typing import TYPE_CHECKING

from fastapi_users import BaseUserManager, IntegerIDMixin
from fastapi_users.db import BaseUserDatabase

from src.mailing import send_email_confirmed, send_verification_email
from src.config import settings
from src.models import UserOrm

if TYPE_CHECKING:
    from fastapi import Request, BackgroundTasks
    from fastapi_users.password import PasswordHelperProtocol

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[UserOrm, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    def __init__(
        self,
        user_db: BaseUserDatabase[UserOrm, int],
        background_tasks: BackgroundTasks,
        password_helper: PasswordHelperProtocol | None = None,
    ):
        super().__init__(user_db, password_helper)
        self.background_tasks = background_tasks

    async def on_after_register(self, user: UserOrm, request: Request | None = None):
        log.info("User %r has registered.", user.id)

    async def on_after_forgot_password(
        self, user: UserOrm, token: str, request: Request | None = None
    ):
        log.info("User %r has forgot their password. Reset token: %r", user.id, token)

    async def on_after_request_verify(
        self, user: UserOrm, token: str, request: Request | None = None
    ):
        log.info(
            "Verification requested for user %r. Verification token: %r", user.id, token
        )
        verification_link = "http://127.0.0.1:8000/docs#/Auth/verify_verify_api_v1_auth_verify_post"
        if self.background_tasks:
            self.background_tasks.add_task(
                send_verification_email,
                user=user,
                verification_link=verification_link,
                verification_token=token,
            )

    async def on_after_verify(
        self, user: UserOrm, request: Request | None = None
    ):
        log.info("User %r has been verified", user.id)
        if self.background_tasks:
            self.background_tasks.add_task(
                send_email_confirmed,
                user=user,
            )
