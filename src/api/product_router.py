from typing import List

from fastapi import APIRouter, HTTPException

from src.handlers.product_handler import ProductHandler
from src.schemas.product import Product, ProductCreate, ProductUpdate

router = APIRouter(prefix="/product", tags=["Product"])


@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: int) -> Product | None:
    product = await ProductHandler.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    return product


@router.get("/", response_model=List[Product])
async def get_all() -> list[Product] | None:
    products = await ProductHandler.get_all()
    if not products:
        raise HTTPException(status_code=404, detail=f"Products not found")
    return products


@router.post("/", response_model=Product)
async def create_product(product: ProductCreate) -> Product:
    return await ProductHandler.create(product)


@router.put("/", response_model=Product)
async def update_product(product: ProductUpdate) -> Product | None:
    updated_product = await ProductHandler.update(product)
    if not updated_product:
        raise HTTPException(status_code=404, detail=f"Product with id {updated_product.id} not found")
    return updated_product


@router.delete("/{product_id}")
async def delete_product(product_id: int) -> None:
    success = await ProductHandler.delete(product_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
