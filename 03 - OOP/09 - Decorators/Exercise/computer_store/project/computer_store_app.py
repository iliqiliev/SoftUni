from typing import Dict, List, Type
from project.computer_types import Computer, DesktopComputer, Laptop


class ComputerStoreApp:
    _COMPUTER_TYPES: Dict[str, Type[Computer]] = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop
    }

    def __init__(self) -> None:
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(  # pylint: disable=too-many-arguments
        self,
        type_computer: str,
        manufacturer: str,
        model: str,
        processor: str,
        ram: int
    ) -> str:

        if type_computer not in self._COMPUTER_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer_class = self._COMPUTER_TYPES[type_computer]

        computer = computer_class(manufacturer, model)
        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return result

    def sell_computer(
        self, client_budget: int, wanted_processor: str, wanted_ram: int
    ) -> str:

        for index, computer in enumerate(self.warehouse):
            if (
                computer.price <= client_budget and
                computer.processor == wanted_processor and
                computer.ram is not None and computer.ram >= wanted_ram
            ):
                break

        else:  # pylint: disable=broad-exception-raised
            raise Exception("Sorry, we don't have a computer for you.")

        profit = client_budget - self.warehouse.pop(index).price
        self.profits += profit

        return f"{computer} sold for {client_budget}$."
