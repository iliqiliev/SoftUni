from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @abstractmethod
    def work(self) -> str: ...


class Worker(BaseWorker):
    def work(self) -> str:
        return "I'm working!!"


class SuperWorker(BaseWorker):
    def work(self) -> str:
        return "I work very hard!!!"


class Manager:
    def __init__(self, worker: BaseWorker) -> None:
        self.worker = worker

    @property
    def worker(self) -> BaseWorker:
        return self.__worker

    @worker.setter
    def worker(self, worker: BaseWorker) -> None:
        if not isinstance(worker, BaseWorker):
            raise ValueError(f"Worker must be {BaseWorker}")

        self.__worker = worker

    def delegate_work(self) -> None:
        print(self.worker.work())


def main():
    manager = Manager(Worker())
    manager.delegate_work()

    manager.worker = SuperWorker()
    manager.delegate_work()


if __name__ == "__main__":
    main()
