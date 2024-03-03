from project.vehicle import Vehicle


class Car(Vehicle):  # pylint: disable=too-few-public-methods
    def drive(self) -> str:
        return "driving..."
