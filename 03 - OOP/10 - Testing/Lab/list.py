from unittest import TestCase, main


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.list = IntegerList(0, 1, 2.0, -3, 4.5, "6", complex(7), [8])

    def test_init(self) -> None:
        self.assertEqual([0, 1, -3], self.list.get_data())

    def test_add_method(self) -> None:
        self.list.add(505)

        self.assertEqual(505, self.list.get_data()[-1])

    def test_add_not_int_raises_exception(self) -> None:
        with self.assertRaises(ValueError) as error:
            self.list.add("6 6 6")

        self.assertEqual("Element is not Integer", str(error.exception))

    def test_remove_index_method(self) -> None:
        index = -1

        self.assertEqual(-3, self.list.remove_index(index))
        self.assertEqual([0, 1], self.list.get_data())

    def test_remove_index_method_wrong_index(self) -> None:
        wrong_index = len(self.list.get_data())

        with self.assertRaises(IndexError) as error:
            self.list.remove_index(wrong_index)

        self.assertEqual("Index is out of range", str(error.exception))

    def test_get_method(self) -> None:
        index = 2

        self.assertEqual(-3, self.list.get(index))

    def test_get_method_wrong_index(self) -> None:
        wrong_index = len(self.list.get_data())

        with self.assertRaises(IndexError) as error:
            self.list.get(wrong_index)

        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert_method(self) -> None:
        index = 0
        element = 100

        self.list.insert(index, element)

        self.assertEqual(element, self.list.get_data()[index])

    def test_insert_method_wrong_input(self) -> None:
        index = 100
        element = 100

        with self.assertRaises(IndexError) as error:
            self.list.insert(index, element)

        self.assertEqual("Index is out of range", str(error.exception))

        index = 0
        element = "100"

        with self.assertRaises(ValueError) as error:
            self.list.insert(index, element)

        self.assertEqual("Element is not Integer", str(error.exception))

    def test_get_biggest_method(self) -> None:
        self.assertEqual(1, self.list.get_biggest())

    def test_get_index_method(self) -> None:
        element = -3

        self.assertEqual(2, self.list.get_index(element))

    def test_get_big_negative_index(self) -> None:
        index = -100

        with self.assertRaises(IndexError) as error:
            self.list.get(index)

        self.assertEqual("Index is out of range", str(error.exception))


if __name__ == "__main__":
    main()
