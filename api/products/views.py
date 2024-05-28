from typing import Any

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.products.serializers import ProductsViewSerializer
from products.services import DefaultProductsServices


class ProductsView(APIView):
    serializer_class = ProductsViewSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        pass

    @extend_schema(
        responses={status.HTTP_201_CREATED: serializer_class},
    )
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Create new product"""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # TODO: containerize services -> eg. container().default_products_services.create_new_product()
        result = DefaultProductsServices.create_new_product(serializer.validated_data)
        return Response(self.serializer_class(result).data, status=status.HTTP_201_CREATED)
