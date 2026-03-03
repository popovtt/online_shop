from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import product_router


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