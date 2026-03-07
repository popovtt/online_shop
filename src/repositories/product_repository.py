from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.product import ProductOrm
from src.repositories.base_repository import BaseRepository
from src.schemas.product import Product, ProductCreate, ProductUpdate


class ProductRepository(BaseRepository):
    async def get_by_id(self, product_id: int, session: AsyncSession) -> Product | None:
        if orm_product := await self._get_orm_entity(product_id, ProductOrm, session):
            return orm_product.to_product()
        return None

    @staticmethod
    async def get_all(session: AsyncSession) -> list[Product] | None:
        stmt = select(ProductOrm)
        result = await session.execute(stmt)
        return [product.to_product() for product in result.scalars().all()]

    @staticmethod
    async def create(
        product_create: ProductCreate, session: AsyncSession
    ) -> Product:
        orm_product = ProductOrm.from_product(product_create)
        session.add(orm_product)

        await session.commit()
        await session.refresh(orm_product)

        return orm_product.to_product()

    async def update(
        self, product_update: ProductUpdate, session: AsyncSession
    ) -> Product | None:
        orm_product = await self._get_orm_entity(product_update.id, ProductOrm, session)
        if not orm_product:
            return None

        await self._update_entity_base_fields(orm_product, product_update.model_dump())

        await session.commit()
        await session.refresh(orm_product)

        return orm_product.to_product()

    async def delete(
        self, product_id: int, session: AsyncSession
    ) -> bool:
        if not (orm_product := await self._get_orm_entity(product_id, ProductOrm, session)):
            return False

        await session.delete(orm_product)
        await session.flush()
        await session.commit()
        return True
