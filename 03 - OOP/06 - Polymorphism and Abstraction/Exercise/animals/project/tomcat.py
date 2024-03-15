from project import Cat


class Tomcat(Cat):
    _SOUND = "Hiss"

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, "Male")
