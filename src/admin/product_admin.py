from sqladmin import ModelView

from src.models.product import ProductOrm


class ProductAdmin(ModelView, model=ProductOrm):
    column_list = [
        "id",
        "title",
        "description",
        "price",
        "category",
    ]