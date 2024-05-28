from typing import Optional

from uuid import UUID

from products.models import Product
from products.selectors import ProductSelector


class DefaultProductsServices:
    """Service used in API, expected valid data"""

    @staticmethod
    def create_new_product(data: dict) -> Product:
        return Product.objects.create(**data)

    @staticmethod
    def update_existing_product(update_data: dict, search_params: dict) -> Optional[Product]:
        if product_id := search_params["product_id"]:
            products = ProductSelector.filter_by_uuid(product_id)
            products.update(**update_data)
            return products.first()
        else:
            return None

    @staticmethod
    def delete_product_by_id(product_id: UUID) -> bool:
        if product := ProductSelector.get_by_uuid(product_id):
            product.delete()
            return True
        return False
