from typing import Any

from rest_framework.request import Request
from rest_framework.response import Response

from api.products.serializers import ProductsViewSerializer


class ProductsView:
    serializer_class = ProductsViewSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        pass
