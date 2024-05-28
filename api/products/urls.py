from django.urls import path

from api.products.views import SingleProductsView, ProductsView

urlpatterns = [
    path("", ProductsView.as_view(), name="products"),
    path("<product_id>", SingleProductsView.as_view(), name="product-delete"),
]
