from command import Command


class Button:
    def __init__(self, command: Command) -> None:
        self.command = command

    def click(self) -> None:
        self.command.execute()


class KeyboardShortcut:
    def __init__(self, command: Command, combination: list[str]) -> None:
        self.command = command
        self.combination = combination

    def press(self, combination: list[str]) -> None:
        if combination == self.combination:
            self.command.execute()
