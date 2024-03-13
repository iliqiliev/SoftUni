from calendar import month_name


class DVD:
    def __init__(  # pylint: disable=too-many-arguments
        self,
        name: str,
        id_: int,
        creation_year: int,
        creation_month: str,
        age_restriction: int
    ) -> None:

        self.name = name
        self.id = id_
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(
        cls, id_: int, name: str, date: str, age_restriction: int
    ) -> "DVD":

        _, month, year = map(int, date.split("."))
        month = month_name[month]

        return cls(name, id_, year, month, age_restriction)

    def __repr__(self) -> str:
        status = f"{'not ' * (not self.is_rented)}rented"

        return (
            f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) "
            f"has age restriction {self.age_restriction}. Status: {status}"
        )
