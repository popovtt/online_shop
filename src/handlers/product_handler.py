from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.product_repository import ProductRepository
from src.schemas.product import Product, ProductCreate, ProductUpdate


class ProductHandler:
    __repository = ProductRepository()

    @classmethod
    async def get_by_id(cls, product_id: int, session: AsyncSession) -> Product | None:
        return await cls.__repository.get_by_id(product_id, session)

    @classmethod
    async def get_all(cls, session: AsyncSession) -> list[Product] | None:
        return await cls.__repository.get_all(session)

    @classmethod
    async def create(cls, product: ProductCreate, session: AsyncSession) -> Product:
        return await cls.__repository.create(product, session)

    @classmethod
    async def update(
        cls, product: ProductUpdate, session: AsyncSession
    ) -> Product | None:
        return await cls.__repository.update(product, session)

    @classmethod
    async def delete(cls, product_id: int, session: AsyncSession) -> bool:
        return await cls.__repository.delete(product_id, session)
