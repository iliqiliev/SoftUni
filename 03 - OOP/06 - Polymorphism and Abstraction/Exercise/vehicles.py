from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, km): ...

    @abstractmethod
    def refuel(self, fuel): ...


class Car(Vehicle):
    _SUMMER_AC_INCREASE = 0.9

    def drive(self, km: float) -> None:
        needed_fuel = (self.fuel_consumption + self._SUMMER_AC_INCREASE) * km

        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    _SUMMER_AC_INCREASE = 1.6
    _GAS_TANK_HOLE = 0.05

    def drive(self, km: float) -> None:
        needed_fuel = (self.fuel_consumption + self._SUMMER_AC_INCREASE) * km

        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * (1 - self._GAS_TANK_HOLE)
