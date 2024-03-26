from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self) -> None:
        self.car = Car("VW", "Golf", 5, 55)

    def test_init(self):
        self.assertEqual("VW", self.car.make)
        self.assertEqual("Golf", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(55, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_wrong_init(self):
        with self.assertRaises(Exception) as error:
            Car("", "Golf", 5, 55)

        self.assertEqual(
            "Make cannot be null or empty!", str(error.exception)
        )

        with self.assertRaises(Exception) as error:
            Car("VW", "", 5, 55)

        self.assertEqual(
            "Model cannot be null or empty!", str(error.exception)
        )

        with self.assertRaises(Exception) as error:
            Car("VW", "Golf", -20, 55)

        self.assertEqual(
            "Fuel consumption cannot be zero or negative!", str(error.exception)
        )

        with self.assertRaises(Exception) as error:
            Car("VW", "Golf", 5, -0.2)

        self.assertEqual(
            "Fuel capacity cannot be zero or negative!", str(error.exception)
        )

    def test_fuel_amount(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_amount = -1

        self.assertEqual(
            "Fuel amount cannot be negative!", str(error.exception)
        )

        self.car.fuel_amount = 123

        self.assertEqual(123, self.car.fuel_amount)

    def test_refuel(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(0)

        self.assertEqual(
            "Fuel amount cannot be zero or negative!", str(error.exception)
        )

        self.car.refuel(10)

        self.assertEqual(10, self.car.fuel_amount)

        self.car.refuel(float("inf"))

        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_drive(self):
        with self.assertRaises(Exception) as error:
            self.car.drive(100)

        self.assertEqual(
            "You don't have enough fuel to drive!", str(error.exception)
        )

        self.car.refuel(5.5)

        self.car.drive(100)

        self.assertEqual(0.5, self.car.fuel_amount)


if __name__ == "__main__":
    main()
