from abc import ABC, abstractmethod
from command import GUIWindow


class Command(ABC):
    def __init__(self, receiver: GUIWindow) -> None:
        self.receiver = receiver

    @abstractmethod
    def execute(self) -> None: ...


class SaveCommand(Command):
    def execute(self) -> None:
        self.receiver.saved = True


class CloseCommand(Command):
    def execute(self) -> None:
        self.receiver.saved = False
        self.receiver.minimized = False


class MinimizeCommand(Command):
    def execute(self) -> None:
        self.receiver.minimized = not self.receiver.minimized
