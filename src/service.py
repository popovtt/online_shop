from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from src.config import settings
from src.admin import ProductAdmin, UserAdmin
from src.api import product_router, auth_router, users_router

from src.utils.db_helper import db_helper


class AppService(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        api_prefix = f"{settings.api.prefix}{settings.api.v1.prefix}"

        # Register router
        self.include_router(product_router, prefix=api_prefix)
        self.include_router(auth_router, prefix=api_prefix)
        self.include_router(users_router, prefix=api_prefix)

        # Register admin
        self.admin = Admin(self, db_helper.engine)
        self.admin.add_view(ProductAdmin)
        self.admin.add_view(UserAdmin)
