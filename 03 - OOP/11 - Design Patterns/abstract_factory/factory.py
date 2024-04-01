from abc import ABC, abstractmethod
from abstract_factory import Chair, Sofa, Table


class AbstractFactory(ABC):
    @property
    @abstractmethod
    def style(self) -> str: ...

    def create_chair(self) -> Chair:
        return Chair(self.style)

    def create_sofa(self) -> Sofa:
        return Sofa(self.style)

    def create_table(self) -> Table:
        return Table(self.style)


class VictorianFactory(AbstractFactory):
    @property
    def style(self) -> str:
        return "Victorian"


class ModernFactory(AbstractFactory):
    @property
    def style(self) -> str:
        return "Modern"


class FuturisticFactory(AbstractFactory):
    @property
    def style(self) -> str:
        return "Futuristic"
