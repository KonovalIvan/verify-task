from typing import Any
from django_filters import ChoiceFilter, FilterSet

from products.models import ProductCategory, Product


class ProductFilter(FilterSet):
    category = ChoiceFilter(
        choices=ProductCategory,
        method="filter_by_category",
    )

    def filter_by_category(self, queryset: Any, name: Any, value: Any) -> Any:
        return queryset.filter(category=value)

    class Meta:
        model = Product
        fields = ["category", ]
