from enum import StrEnum

from pydantic import BaseModel, ConfigDict, field_validator


class Category(StrEnum):
    clothes = "Clothes"
    boots = "Boots"
    bags = "Bags"
    accessories = "Accessories"


class ProductCreate(BaseModel):
    title: str
    description: str
    price: float
    category: Category

    @field_validator("title")
    @classmethod
    def title_validator(cls, value: str) -> str:
        if len(value) < 4:
            raise ValueError(
                "Title must be at least 4 characters long"
            )  # Correct for v2
        return value


class ProductUpdate(ProductCreate):
    id: int


class Product(ProductUpdate):
    model_config = ConfigDict(from_attributes=True)
