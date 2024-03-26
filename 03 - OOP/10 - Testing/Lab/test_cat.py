from unittest import TestCase, main


class WorkerCat(TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Pori")

    def test_worker_init(self) -> None:
        self.assertEqual("Pori", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_overfeeding_raises_exception(self) -> None:
        self.cat.fed = True

        with self.assertRaises(Exception) as error:
            self.cat.eat()

        self.assertEqual("Already fed.", str(error.exception))

    def test_feeding_makes_fed_sleepy_and_increases_size(self) -> None:
        target_size = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(target_size, self.cat.size)

    def test_sleeping_hungry_raises_exception(self) -> None:
        with self.assertRaises(Exception) as error:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(error.exception))

    def test_sleepy_cat_sleeps_succsleepfully_and_sleepily(self) -> None:
        self.cat.eat()

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
