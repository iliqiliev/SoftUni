from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.v = Vehicle(1.5, 3)

    def test_init(self) -> None:
        self.assertEqual(1.5, self.v.fuel)
        self.assertEqual(1.5, self.v.capacity)
        self.assertEqual(3, self.v.horse_power)
        self.assertEqual(1.25, self.v.fuel_consumption)

    def test_drive_not_enough_fuel(self) -> None:
        with self.assertRaises(Exception) as error:
            self.v.drive(100)

        self.assertEqual("Not enough fuel", str(error.exception))

    def test_drive_enough_fuel(self) -> None:
        distance = 1
        target_fuel = self.v.fuel - distance * self.v.fuel_consumption

        self.v.drive(distance)

        self.assertEqual(target_fuel, self.v.fuel)

    def test_refuel_too_much_fuel(self) -> None:
        with self.assertRaises(Exception) as error:
            self.v.refuel(100)

        self.assertEqual("Too much fuel", str(error.exception))

    def test_refuel_within_capacity(self) -> None:
        self.v.fuel = 0
        refuel = 1
        target_fuel = self.v.fuel + refuel

        self.v.refuel(refuel)

        self.assertEqual(target_fuel, self.v.fuel)

    def test_string_representation_method(self) -> None:
        self.assertEqual(
            f"The vehicle has {self.v.horse_power} horse power with "
            f"{self.v.fuel} fuel left and {self.v.fuel_consumption} fuel consumption",

            str(self.v)
        )


if __name__ == "__main__":
    main()
