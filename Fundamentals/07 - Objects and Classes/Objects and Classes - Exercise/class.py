class Class:
    __student_count = 22

    def __init__(self, name) -> None:
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, student_name: str, grade: float) -> bool:
        if len(self.students) < Class.__student_count:
            self.students.append(student_name)
            self.grades.append(grade)
            return True

        return False

    def get_average_grade(self) -> float:
        if len(self.students):
            return sum(self.grades) / len(self.grades)

        else:
            return 0

    def __str__(self) -> str:
        student_names = ', '.join(self.students)
        return f"The students in {self.name}: {student_names}. Average grade: {self.get_average_grade():.2f}"
