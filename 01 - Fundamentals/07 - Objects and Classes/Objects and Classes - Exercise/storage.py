class Storage:
    storage = []

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity

    def add_product(self, product: str) -> bool:
        if self.capacity > len(Storage.storage):
            Storage.storage.append(product)
            return True
        
        return False

    def get_products(self) -> list:
        return Storage.storage
