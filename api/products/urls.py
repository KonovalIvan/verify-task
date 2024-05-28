from django.urls import path

from api.products.views import ProductsView

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products')
]
