from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class ClimbingRobotTest(TestCase):
    def setUp(self) -> None:
        self.robot = ClimbingRobot("Alpine", "part", 10, 12)

    def test_init(self) -> None:
        self.assertEqual("Alpine", self.robot.category)
        self.assertEqual("part", self.robot.part_type)
        self.assertEqual(10, self.robot.capacity)
        self.assertEqual(12, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_check_allowed_categories(self) -> None:
        self.assertEqual(
            ['Mountain', 'Alpine', 'Indoor', 'Bouldering'],
            ClimbingRobot.ALLOWED_CATEGORIES
        )

    def test_category_setter_invalid(self) -> None:
        with self.assertRaises(ValueError) as error:
            self.robot.category = "Инжекопляктор"

        self.assertEqual(
            f"Category should be one of {self.robot.ALLOWED_CATEGORIES}",
            str(error.exception)
        )

    def test_get_used_capacity(self) -> None:
        self.assertEqual(0, self.robot.get_used_capacity())

        self.robot.installed_software = [
            {"1": "name", "capacity_consumption": 1, "memory_consumption": 4},
            {"2": "name", "capacity_consumption": 2, "memory_consumption": 5},
            {"3": "name", "capacity_consumption": 3, "memory_consumption": 6},
        ]

        self.assertEqual(6, self.robot.get_used_capacity())

    def test_get_used_memory(self) -> None:
        self.assertEqual(0, self.robot.get_used_memory())

        self.robot.installed_software = [
            {"1": "name", "capacity_consumption": 1, "memory_consumption": 4},
            {"2": "name", "capacity_consumption": 2, "memory_consumption": 5},
            {"3": "name", "capacity_consumption": 3, "memory_consumption": 6},
        ]

        self.assertEqual(15, self.robot.get_used_memory())

    def test_get_available_capacity(self) -> None:
        self.robot.installed_software = [
            {"1": "name", "capacity_consumption": 1, "memory_consumption": 4},
            {"2": "name", "capacity_consumption": 2, "memory_consumption": 5},
            {"3": "name", "capacity_consumption": 3, "memory_consumption": 6},
        ]

        self.assertEqual(4, self.robot.get_available_capacity())

    def test_get_available_memory(self) -> None:
        self.robot.memory = 15

        self.robot.installed_software = [
            {"1": "name", "capacity_consumption": 1, "memory_consumption": 4},
            {"2": "name", "capacity_consumption": 2, "memory_consumption": 5},
            {"3": "name", "capacity_consumption": 3, "memory_consumption": 6},
        ]

        self.assertEqual(0, self.robot.get_available_memory())

    def test_install_software_success(self) -> None:
        software = {
            "name": "1", "capacity_consumption": 1, "memory_consumption": 1
        }

        self.assertEqual(
            f"Software '{software['name']}' successfully "
            f"installed on {self.robot.category} part.",

            self.robot.install_software(software)
        )

        self.assertEqual([software], self.robot.installed_software)

    def test_install_software_fail_one_bigger_than_max(self) -> None:
        software = {
            "name": "1", "capacity_consumption": 12, "memory_consumption": 17
        }

        self.robot.capacity = 100
        self.robot.memory = 10

        self.assertEqual(
            f"Software '{software['name']}' cannot be installed "
            f"on {self.robot.category} part.",

            self.robot.install_software(software)
        )

        self.assertEqual([], self.robot.installed_software)

        self.robot.capacity = 10
        self.robot.memory = 100

        self.assertEqual(
            f"Software '{software['name']}' cannot be installed "
            f"on {self.robot.category} part.",

            self.robot.install_software(software)
        )

        self.assertEqual([], self.robot.installed_software)

    def test_install_software_border_case(self) -> None:
        software = {
            "name": "1", "capacity_consumption": 10, "memory_consumption": 10
        }

        self.robot.capacity = 10
        self.robot.memory = 10

        self.assertEqual(
            f"Software '{software['name']}' successfully "
            f"installed on {self.robot.category} part.",

            self.robot.install_software(software)
        )

        self.assertEqual([software], self.robot.installed_software)


if __name__ == "__main__":
    main()
