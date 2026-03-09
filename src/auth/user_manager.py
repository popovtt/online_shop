import logging

from fastapi import Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from src.config import settings
from src.models import UserOrm

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[UserOrm, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

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
