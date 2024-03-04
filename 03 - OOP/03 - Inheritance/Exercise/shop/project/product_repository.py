from typing import List
from project import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for product in self.products:
            if product.name == product_name:
                return product

        raise LookupError(f"{product_name} not in the repository!")

    def remove(self, product_name: str) -> None:
        for index, product in enumerate(self.products):
            if product.name == product_name:
                self.products.pop(index)
                return

    def __str__(self) -> str:
        return "\n".join(
            f"{product.name}: {product.quantity}" for product in self.products
        )
