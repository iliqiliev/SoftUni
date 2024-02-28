class Employee:
    def __init__(
        self, _id: int, first_name: str, last_name: str, salary: int
    ) -> None:

        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self) -> int:
        return 12 * self.salary

    def raise_salary(self, increase: int) -> int:
        self.salary += increase

        return self.salary
