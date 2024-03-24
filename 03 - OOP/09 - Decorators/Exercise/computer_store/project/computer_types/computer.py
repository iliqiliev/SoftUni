from abc import ABC, abstractmethod
from math import log2
from typing import Dict, Optional


class Computer(ABC):  # pylint: disable=too-many-instance-attributes
    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price: int = 0

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str) -> None:
        if not manufacturer.strip():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = manufacturer

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str) -> None:
        if not model.strip():
            raise ValueError("Model name cannot be empty.")

        self.__model = model

    @property
    def processor(self) -> Optional[str]:
        return self.__processor

    @processor.setter
    def processor(self, processor: Optional[str]) -> None:
        if processor and processor not in self._valid_processors:
            raise ValueError(
                f"{processor} is not compatible with "
                f"{self._nickname} {self.manufacturer} {self.model}!"
            )

        self.__processor = processor

    @property
    def ram(self) -> Optional[int]:
        return self.__ram

    @ram.setter
    def ram(self, ram: Optional[int]) -> None:
        if ram is not None and (
            ram == 0 or
            ram & (ram - 1) or  # bitwise power of 2 check
            ram > self._max_ram
        ):
            raise ValueError(
                f"{ram}GB RAM is not compatible with "
                f"{self._nickname} {self.manufacturer} {self.model}!"
            )

        self.__ram = ram

    @property
    @abstractmethod
    def _valid_processors(self) -> Dict[str, int]: ...

    @property
    @abstractmethod
    def _max_ram(self) -> int: ...

    @property
    @abstractmethod
    def _nickname(self) -> str: ...

    def configure_computer(self, processor: str, ram: int) -> str:
        RAM_PRICE_COEFFICIENT = 100

        self.processor = processor
        self.ram = ram

        self.price = (
            self._valid_processors[processor] +
            int(log2(ram)) * RAM_PRICE_COEFFICIENT
        )

        return f"Created {self} for {self.price}$."

    def __str__(self) -> str:
        return (
            f"{self.manufacturer} {self.model} with "
            f"{self.processor} and {self.ram}GB RAM"
        )
