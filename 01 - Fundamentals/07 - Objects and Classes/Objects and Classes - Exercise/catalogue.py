class Catalogue:

    def __init__(self, name: str) -> None:
        self.name = name
        self.products = []

    def add_product(self, product_name: str) -> None:
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str) -> list:
        return [product for product in self.products if product[0] == first_letter]

    def __str__(self) -> str:
        return (f"Items in the {self.name} catalogue:\n"
                + "\n".join(sorted(self.products)))
