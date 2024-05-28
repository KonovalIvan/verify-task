from django.urls import path

from api.products.views import DeleteProductsView, ProductsView

urlpatterns = [
    path("", ProductsView.as_view(), name="products"),
    path("<product_id>", DeleteProductsView.as_view(), name="product-delete"),
]
