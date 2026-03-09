from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.base import Base


class BaseRepository:
    @staticmethod
    async def _get_orm_entity(
        entity_id: int, orm_model: type[Base], session: AsyncSession
    ):
        stmt = select(orm_model).where(orm_model.id == entity_id)  # type: ignore
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def _update_entity_base_fields(
        orm_entity: type[Base], updated_entity: dict
    ) -> None:
        for field, value in updated_entity.items():
            setattr(orm_entity, field, value)
