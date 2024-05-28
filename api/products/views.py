from typing import Any
from uuid import UUID

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.products.serializers import ProductsQuerySerializer, ProductsViewSerializer, AllProductsViewSerializer, \
    ProductsListFiltersSerializer
from products.models import Product, ProductCategory
from products.selectors import ProductSelector
from products.services import DefaultProductsServices


class ProductsView(APIView):
    serializer_class = ProductsViewSerializer

    @extend_schema(
            responses={status.HTTP_200_OK: AllProductsViewSerializer(many=True)},
            parameters=[
                OpenApiParameter(
                        name="category",
                        type=OpenApiTypes.STR,
                        enum=ProductCategory,
                        required=False,
                ), ]
    )
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer_class = AllProductsViewSerializer

        query = ProductsListFiltersSerializer(data=request.query_params)
        query.is_valid(raise_exception=True)
        result = ProductSelector.filter_by_category(query.validated_data)

        return Response(serializer_class(result, many=True).data, status=status.HTTP_200_OK)

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
        return Response(
                {"error_msg": "Failed to find a product."}, status=status.HTTP_404_NOT_FOUND,
                exception=Product.DoesNotExist
        )


class SingleProductsView(APIView):
    serializer_class = ProductsViewSerializer

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

    @extend_schema(
            responses={status.HTTP_200_OK: serializer_class},
    )
    def get(self, request: Request, product_id: UUID, *args: Any, **kwargs: Any) -> Response:
        """Get single product"""
        if product := ProductSelector.get_by_uuid(uuid=product_id):
            return Response(self.serializer_class(product).data, status=status.HTTP_200_OK)
        return Response(
                {"error_msg": "Failed to find a product."}, status=status.HTTP_404_NOT_FOUND,
                exception=Product.DoesNotExist
        )
