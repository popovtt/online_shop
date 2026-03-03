from sqlalchemy import select

from src.models.product import ProductOrm
from src.repositories.base_repository import BaseRepository
from src.schemas.product import Product, ProductCreate, ProductUpdate


class ProductRepository(BaseRepository):
    async def get_by_id(self, product_id: int) -> Product | None:
        async with self._get_session() as session:
            if orm_product := await self._get_orm_entity(product_id, ProductOrm, session):
                return orm_product.to_product()
            return None

    async def get_all(self) -> list[Product] | None:
        async with self._get_session() as session:
            stmt = select(ProductOrm)
            result = await session.execute(stmt)
            return [product.to_product() for product in result.scalars().all()]

    async def create(self, product_create: ProductCreate) -> Product:
        async with self._get_session() as session:
            orm_product = ProductOrm.from_product(product_create)
            session.add(orm_product)

            await session.commit()
            await session.refresh(orm_product)

            return orm_product.to_product()

    async def update(self, product_update: ProductUpdate) -> Product | None:
        async with self._get_session() as session:
            orm_product = await self._get_orm_entity(product_update.id, ProductOrm, session)
            if not orm_product:
                return None

            await self._update_entity_base_fields(orm_product, product_update.model_dump())

            await session.commit()
            await session.refresh(orm_product)

            return orm_product.to_product()

    async def delete(self, product_id: int) -> bool:
        async with self._get_session() as session:
            if not (orm_product := await self._get_orm_entity(product_id, ProductOrm, session)):
                return False

            await session.delete(orm_product)
            await session.flush()
            await session.commit()
            return True
