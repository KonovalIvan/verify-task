from typing import Any

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from uuid import UUID

from api.products.serializers import ProductsQuerySerializer, ProductsViewSerializer
from products.models import Product
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

    @extend_schema(
        responses={status.HTTP_200_OK: serializer_class},
        parameters=[
            OpenApiParameter("product_id", OpenApiTypes.UUID, description="Find product by id"),
        ],
    )
    def put(self, request: Request) -> Response:
        """Update existing product"""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        query_params = ProductsQuerySerializer(data=request.query_params)
        query_params.is_valid(raise_exception=True)

        if result := DefaultProductsServices.update_existing_product(
            serializer.validated_data, query_params.validated_data
        ):
            return Response(self.serializer_class(result).data, status=status.HTTP_200_OK)
        return Response({"error_msg": "Failed to find a product."},
                        status=status.HTTP_404_NOT_FOUND,
                        exception=Product.DoesNotExist)


class DeleteProductsView(APIView):
    @extend_schema(
        responses={status.HTTP_204_NO_CONTENT},
    )
    def delete(self, request: Request, product_id: UUID, *args: Any, **kwargs: Any) -> Response:
        """Delete product"""
        success = DefaultProductsServices.delete_product_by_id(product_id=product_id)

        return (
            Response(status=status.HTTP_204_NO_CONTENT)
            if success
            else Response({"error_msg": "Failed to find a product."}, status=status.HTTP_404_NOT_FOUND)
        )