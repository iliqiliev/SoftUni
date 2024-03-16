from __future__ import annotations
from abc import ABC, abstractmethod


class PowerSource:
    pass


class Connectable(ABC):
    @abstractmethod
    def connect(self, device: Connectable): ...

    @abstractmethod
    def connect_power(self, power_source: PowerSource): ...


class EntertainmentDevice(Connectable):
    def __init__(self, power_source: PowerSource) -> None:
        self.connect_power(power_source)


class HDMIMixin(Connectable):
    ...


class RCAMixin(Connectable):
    ...


class EthernetMixin(Connectable):
    ...


class Television(EntertainmentDevice, HDMIMixin, RCAMixin):
    ...


class DVDPlayer(EntertainmentDevice, HDMIMixin):
    ...


class GameConsole(EntertainmentDevice, HDMIMixin, EthernetMixin):
    ...


class Router(EntertainmentDevice, EthernetMixin):
    ...
