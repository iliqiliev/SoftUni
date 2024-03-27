from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Pori", "Cat", "Meow")

    def test_init(self) -> None:
        self.assertEqual("Pori", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("Meow", self.mammal.sound)

    def test_get_kingdom_method(self) -> None:
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound(self) -> None:
        self.assertEqual(
            f"{self.mammal.name} makes {self.mammal.sound}",
            self.mammal.make_sound()
        )

    def test_info_method(self) -> None:
        self.assertEqual(
            f"{self.mammal.name} is of type {self.mammal.type}",
            self.mammal.info()
        )


if __name__ == "__main__":
    main()
