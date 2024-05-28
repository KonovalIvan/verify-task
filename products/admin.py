from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = (
        "name",
        "description",
        "price",
        "amount",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Product, ProductAdmin)
