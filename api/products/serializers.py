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


class ProductsQuerySerializer(serializers.Serializer):
    product_id = serializers.UUIDField(required=False)
