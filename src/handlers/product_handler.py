from src.repositories.product_repository import ProductRepository
from src.schemas.product import Product, ProductCreate, ProductUpdate
from src.utils.db import engine


class ProductHandler:
    __repository = ProductRepository(engine)

    @classmethod
    async def get_by_id(cls, product_id: int) -> Product | None:
        return await cls.__repository.get_by_id(product_id)

    @classmethod
    async def get_all(cls) -> list[Product] | None:
        return await cls.__repository.get_all()

    @classmethod
    async def create(cls, product: ProductCreate) -> Product:
        return await cls.__repository.create(product)

    @classmethod
    async def update(cls, product: ProductUpdate) -> Product | None:
        return await cls.__repository.update(product)

    @classmethod
    async def delete(cls, product_id: int) -> bool:
        return await cls.__repository.delete(product_id)
