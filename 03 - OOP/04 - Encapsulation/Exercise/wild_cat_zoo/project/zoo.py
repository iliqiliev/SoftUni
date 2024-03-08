from collections import defaultdict
from typing import Dict, List, Union
from project import Animal, Worker


class Zoo:
    def __init__(
        self, name: str, budget: int, animal_capacity: int, workers_capacity: int
    ) -> None:

        self.name = name
        self.__budget = budget

        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.__animal_types = defaultdict(list)
        self.__worker_types = defaultdict(list)

        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        self.__sort_entry(self.__animal_types, animal)

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        self.__sort_entry(self.__worker_types, worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        for index, worker in enumerate(self.workers):
            if worker.name == worker_name:
                break

        else:
            return f"There is no {worker_name} in the zoo"

        fired = self.workers.pop(index)
        self.__worker_types[fired.__class__.__name__].remove(fired)

        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        worker_salaries = sum(worker.salary for worker in self.workers)

        if self.__budget < worker_salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= worker_salaries

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        animal_upkeep = sum(animal.money_for_care for animal in self.animals)

        if self.__budget < animal_upkeep:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animal_upkeep

        return (
            "You tended all the animals. They are happy. "
            f"Budget left: {self.__budget}"
        )

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def __generate_entry(
        self, catalog: Dict[str, List[Union[Worker, Animal]]], *categories: str
    ) -> str:
        result = []

        for category in categories:
            result.append(f"----- {len(catalog[category])} {category}s:")
            result.extend(str(entry) for entry in catalog[category])

        return "\n".join(result)

    def __sort_entry(
        self,
        catalog: Dict[str, List[Union[Worker, Animal]]],
        entry: Union[Worker, Animal]
    ) -> None:

        catalog[entry.__class__.__name__].append(entry)

    def animals_status(self) -> str:
        return (
            f"You have {len(self.animals)} animals\n" +
            self.__generate_entry(self.__animal_types, "Lion", "Tiger", "Cheetah")
        )

    def workers_status(self) -> str:
        return (
            f"You have {len(self.workers)} workers\n" +
            self.__generate_entry(self.__worker_types, "Keeper", "Caretaker", "Vet")
        )
