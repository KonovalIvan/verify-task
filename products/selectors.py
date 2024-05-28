from typing import Any, Dict, Optional
from uuid import UUID

from django.db.models import QuerySet

from products.filters import ProductFilter
from products.models import Product


class ProductSelector:
    @staticmethod
    def filter_by_uuid(uuid: UUID) -> QuerySet[Product]:
        return Product.objects.filter(id=uuid)

    @staticmethod
    def filter_by_name(name: str) -> QuerySet[Product]:
        return Product.objects.filter(name=name)

    @staticmethod
    def filter_by_category(filters: Dict[Any, Any]) -> QuerySet[Product]:
        qs = Product.objects.all()
        return ProductFilter(filters, queryset=qs).qs.distinct()

    @staticmethod
    def get_by_uuid(uuid: UUID) -> Optional[Product]:
        try:
            return Product.objects.get(id=uuid)
        except Product.DoesNotExist:
            return None
