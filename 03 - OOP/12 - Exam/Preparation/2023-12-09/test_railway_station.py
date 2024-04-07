from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class RailwayStationTest(TestCase):
    def setUp(self) -> None:
        self.rs = RailwayStation("Tsentralna")
        self.rs_has_trains = RailwayStation("Tsentralna")

        train = "Vidin 1721"
        train2 = "Vidin 2234"

        self.rs_has_trains.arrival_trains = deque([train, train2])

    def test_init(self) -> None:
        self.assertEqual("Tsentralna", self.rs.name)
        self.assertEqual(deque(), self.rs.arrival_trains)
        self.assertEqual(deque(), self.rs.departure_trains)

    def test_wrong_name_raises_value_error(self) -> None:
        with self.assertRaises(ValueError) as error:
            self.rs.name = ""

        self.assertEqual(
            "Name should be more than 3 symbols!", str(error.exception)
        )

    def test_new_arrival_on_board(self) -> None:
        train = "Vidin 1721"
        train2 = "Vidin 2234"

        self.rs.new_arrival_on_board(train)

        self.assertEqual(deque([train]), self.rs.arrival_trains)

        self.rs.new_arrival_on_board(train2)

        self.assertEqual(deque([train, train2]), self.rs.arrival_trains)

    def test_train_arrival_correct_path(self) -> None:
        train = "Vidin 1721"

        self.assertEqual(
            f"{train} is on the platform and will leave in 5 minutes.",
            self.rs_has_trains.train_has_arrived(train)
        )

    def test_train_arrival_incorrect_train_info(self) -> None:
        wrong_train = "aaaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAA"

        self.assertEqual(
            f"There are other trains to arrive before {wrong_train}.",
            self.rs_has_trains.train_has_arrived(wrong_train)
        )

    def test_train_has_left_correct_info(self) -> None:
        self.rs.departure_trains = deque(["1", "2", "3"])

        self.assertTrue(self.rs.train_has_left("1"))
        self.assertEqual(deque(["2", "3"]), self.rs.departure_trains)

    def test_train_has_left_incorrect_train(self) -> None:
        self.rs.departure_trains = deque(["1", "2", "3"])

        self.assertFalse(self.rs.train_has_left("2"))
        self.assertEqual(deque(["1", "2", "3"]), self.rs.departure_trains)


if __name__ == "__main__":
    main()
