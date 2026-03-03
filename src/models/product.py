from typing import Self

from sqlalchemy import Integer, String, Float, Enum
from sqlalchemy.orm import mapped_column, Mapped

from src.models.base import Base
from src.models.mixins.timestamp import TimestampMixin
from src.schemas.product import Category, ProductCreate, Product


class ProductOrm(TimestampMixin, Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    category: Mapped[Category] = mapped_column(
        Enum(Category),
        default=Category.clothes,
        nullable=True
    )

    def to_product(self) -> Product:
        return Product.model_validate(self)

    @classmethod
    def from_product(cls, product: ProductCreate) -> Self:
        return cls(**product.model_dump())
