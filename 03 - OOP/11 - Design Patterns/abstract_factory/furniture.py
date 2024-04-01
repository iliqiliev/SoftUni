from abc import ABC, abstractmethod


class FurnitureBase(ABC):
    def __init__(self, style: str) -> None:
        self.style = style

    @abstractmethod
    def __str__(self) -> str: ...


class Chair(FurnitureBase):
    def __str__(self) -> str:
        return f"{self.style} chair"
    
class Sofa(FurnitureBase):
    def __str__(self) -> str:
        return f"{self.style} sofa"
    
class Table(FurnitureBase):
    def __str__(self) -> str:
        return f"{self.style} table"
