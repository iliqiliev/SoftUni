from project import Person, Employee


class Teacher(Person, Employee):
    def teach(self) -> str:
        return "teaching..."
