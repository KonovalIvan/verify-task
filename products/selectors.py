from uuid import UUID

from django.db.models import QuerySet

from products.models import Product


class ProductSelector:
    @staticmethod
    def filter_by_uuid(uuid: UUID) -> QuerySet[Product]:
        return Product.objects.filter(id=uuid)

    @staticmethod
    def filter_by_name(name: str) -> Product:
        return Product.objects.filter(name=name)
