from typing import Iterable


class Person:
    def __init__(self, position: Iterable[int]) -> None:
        self.position = list(position)


class FreePerson(Person):
    def walk_east(self, distance: int) -> None:
        self.position[0] += distance

    def walk_north(self, distance: int) -> None:
        self.position[1] += distance


class Prisoner(Person):
    __PRISON_LOCATION = (3, 3)

    def __init__(self) -> None:
        super().__init__(self.PRISON_LOCATION)

    @property
    def PRISON_LOCATION(self) -> tuple[int, int]:
        return self.__PRISON_LOCATION


def main():
    prisoner = Prisoner()
    print("The prisoner trying to walk to north by 10 and east by -3.")

    try:
        prisoner.walk_north(10)  # type: ignore
        prisoner.walk_east(-3)  # type: ignore

    except AttributeError:
        pass

    print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
    print(f"The current position of the prisoner: {tuple(prisoner.position)}")


if __name__ == "__main__":
    main()
