from products.models import Product


class DefaultProductsServices:
    @staticmethod
    def create_new_product(data: dict) -> Product:
        return Product.objects.create(**data)
