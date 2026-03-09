__all__ = [
    "product_router",
    "auth_router",
    "users_router",
]

from src.api.product_router import router as product_router
from src.api.auth_router import router as auth_router
from src.api.users_router import router as users_router
