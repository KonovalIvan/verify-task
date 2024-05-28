from rest_framework import serializers

from products.models import Product


class ProductsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'amount',
        ]
