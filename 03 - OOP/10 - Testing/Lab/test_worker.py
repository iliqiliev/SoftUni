from unittest import TestCase, main


class WorkerTests(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Iliya", 981, 3)

    def test_worker_init(self) -> None:
        self.assertEqual("Iliya", self.worker.name)
        self.assertEqual(981, self.worker.salary)
        self.assertEqual(3, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_incremented_after_resting(self) -> None:
        target_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(target_energy, self.worker.energy)

    def test_work_raises_exception_when_working_with_no_energy(self) -> None:
        self.worker.energy = 0

        with self.assertRaises(Exception) as error:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(error.exception))

        self.worker.energy = -1

        with self.assertRaises(Exception) as error:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(error.exception))

    def test_worker_salary_increased_after_working(self) -> None:
        target_money = self.worker.money + self.worker.salary

        self.worker.work()

        self.assertEqual(target_money, self.worker.money)

    def test_worker_energy_decrements_after_working(self) -> None:
        target_energy = self.worker.energy - 1

        self.worker.work()

        self.assertEqual(target_energy, self.worker.energy)

    def test_worker_get_info_method(self) -> None:
        target = f"{self.worker.name} has saved {self.worker.money} money."

        self.assertEqual(target, self.worker.get_info())


if __name__ == "__main__":
    main()
