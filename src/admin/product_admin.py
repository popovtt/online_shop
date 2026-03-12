from sqladmin import ModelView
from sqladmin.filters import OperationColumnFilter

from src.schemas.product import Category
from src.admin.filters import EnumFilter
from src.models.product import ProductOrm


class ProductAdmin(ModelView, model=ProductOrm):
    name = "Product"
    name_plural = "Products"
    icon = "fa-solid fa-shirt"

    column_list = "__all__"
    column_filters = [
        OperationColumnFilter(ProductOrm.title),
        OperationColumnFilter(ProductOrm.price),
        EnumFilter(ProductOrm.category, Category),
    ]
    column_sortable_list = [
        "id",
        "title",
        "price",
        "category",
    ]
    column_searchable_list = ["title"]
    column_filterable_list = [ProductOrm.category]

    form_excluded_columns = ["created_at", "updated_at"]
