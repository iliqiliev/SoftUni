class Mammal:
    __kingdom = "animals"  # ?

    def __init__(self, name: str, _type: str, sound: str) -> None:
        self.name = name
        self.type = _type
        self.sound = sound

    def make_sound(self) -> str:
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self) -> str:
        return self.__kingdom

    def info(self) -> str:
        return f"{self.name} is of type {self.type}"
