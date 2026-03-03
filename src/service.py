from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from src.admin.product_admin import ProductAdmin
from src.api import product_router
from src.utils.db import engine


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

        # Register router
        self.include_router(product_router)
        self.admin = Admin(self, engine)
        self.admin.add_view(ProductAdmin)