from typing import List


class Smartphone:
    def __init__(self, memory: int) -> None:
        self.memory = memory
        self.apps: List[str] = []
        self.is_on = False

    def power(self) -> None:
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int) -> str:
        if self.memory < app_memory:
            return f"Not enough memory to install {app}"

        if not self.is_on:
            return f"Turn on your phone to install {app}"

        self.apps.append(app)
        self.memory -= app_memory

        return f"Installing {app}"

    def status(self) -> str:
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
