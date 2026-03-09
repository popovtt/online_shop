from typing import List, Annotated

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import settings
from src.handlers.product_handler import ProductHandler
from src.schemas.product import Product, ProductCreate, ProductUpdate
from src.utils.db_helper import db_helper

router = APIRouter(prefix=settings.api.v1.products, tags=["Products"])


@router.get("/{product_id}", response_model=Product)
async def get_product(
    product_id: int,
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
) -> Product | None:
    product = await ProductHandler.get_by_id(product_id, session)
    if not product:
        raise HTTPException(
            status_code=404, detail=f"Product with id {product_id} not found"
        )
    return product


@router.get("/", response_model=List[Product])
async def get_all(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
) -> list[Product] | None:
    products = await ProductHandler.get_all(session)
    if not products:
        raise HTTPException(status_code=404, detail="Products not found")
    return products


@router.post("/", response_model=Product)
async def create_product(
    product: ProductCreate,
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
) -> Product:
    return await ProductHandler.create(product, session)


@router.put("/", response_model=Product)
async def update_product(
    product: ProductUpdate,
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
) -> Product | None:
    updated_product = await ProductHandler.update(product, session)
    if not updated_product:
        raise HTTPException(
            status_code=404, detail=f"Product with id {product.id} not found"
        )
    return updated_product


@router.delete("/{product_id}")
async def delete_product(
    product_id: int,
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
) -> None:
    success = await ProductHandler.delete(product_id, session)
    if not success:
        raise HTTPException(
            status_code=404, detail=f"Product with id {product_id} not found"
        )
