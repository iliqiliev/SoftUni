from __future__ import annotations
from abc import ABC, abstractmethod
from bisect import insort


class Component(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self.depth = 0

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @abstractmethod
    def structure(self) -> str: ...

    @property
    def spacer(self) -> str:
        return "  " * self.depth


class File(Component):
    def structure(self) -> str:
        return f"{self.spacer}{self.name}"


class Directory(Component):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.entries: list[Component] = []

    def add_entry(self, entry: Component) -> None:
        entry.depth = self.depth + 1
        insort(self.entries, entry, key=lambda entry: entry.structure())

    def structure(self) -> str:
        result = [f"{self.spacer}<dir> {self.name}"]

        result.extend(entry.structure() for entry in self.entries)

        return "\n".join(result)
