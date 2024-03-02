class Song:  # pylint: disable=too-few-public-methods
    def __init__(self, name: str, length: float, single: bool) -> None:
        self.name = name
        self.length = length
        self.single = single

    def get_info(self) -> str:
        return f"{self.name} - {self.length}"
