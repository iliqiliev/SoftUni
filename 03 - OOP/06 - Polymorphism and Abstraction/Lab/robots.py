class Robot:
    _SENSOR_COUNT = 1

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def sensor_count(cls) -> int:
        return cls._SENSOR_COUNT


class MedicalRobot(Robot):
    _SENSOR_COUNT = 6


class ChefRobot(Robot):
    _SENSOR_COUNT = 4


class WarRobot(Robot):
    _SENSOR_COUNT = 12


def main():
    basic_robot = Robot('Robo')
    da_vinci = MedicalRobot('Da Vinci')
    moley = ChefRobot('Moley')
    griffin = WarRobot('Griffin')

    print(basic_robot.sensor_count())
    print(da_vinci.sensor_count())
    print(moley.sensor_count())
    print(griffin.sensor_count())


if __name__ == "__main__":
    main()
