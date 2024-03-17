from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @abstractmethod
    def work(self) -> None: ...


class Eatable(ABC):
    @abstractmethod
    def eat(self) -> None: ...


class Worker(BaseWorker, Eatable):
    def work(self) -> None:
        print("I'm normal worker. I'm working.")

    def eat(self) -> None:
        print("Lunch break....(5 secs)")


class SuperWorker(BaseWorker, Eatable):
    def work(self) -> None:
        print("I'm super worker. I work very hard!")

    def eat(self) -> None:
        print("Lunch break....(3 secs)")


class Robot(BaseWorker):
    def work(self) -> None:
        print("I'm a robot. I'm working....")


class Manager:
    def __init__(self, *workers: BaseWorker) -> None:
        self.workers = [*workers]

    @property
    def workers(self) -> list[BaseWorker]:
        return self.__workers

    @workers.setter
    def workers(self, workers: list[BaseWorker]) -> None:
        if not all(isinstance(worker, BaseWorker) for worker in workers):
            raise ValueError(f"Workers must be {BaseWorker}")

        self.__workers = workers

    def manage(self) -> None:
        for worker in self.workers:
            worker.work()

    def lunch_break(self) -> None:
        for worker in self.workers:
            if isinstance(worker, Eatable):
                worker.eat()


def main():
    workers = [Worker(), SuperWorker(), Robot()]
    manager = Manager(*workers)

    manager.manage()
    manager.lunch_break()


if __name__ == "__main__":
    main()
