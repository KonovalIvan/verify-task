from rest_framework import serializers

from products.models import Product, ProductCategory


class ProductsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "amount",
            "category",
        ]


class AllProductsViewSerializer(ProductsViewSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
        ] + ProductsViewSerializer.Meta.fields


class ProductsQuerySerializer(serializers.Serializer):
    product_id = serializers.UUIDField(required=False)


class ProductsListFiltersSerializer(serializers.Serializer):
    category = serializers.ChoiceField(choices=ProductCategory, allow_blank=True, allow_null=True, default=None)
