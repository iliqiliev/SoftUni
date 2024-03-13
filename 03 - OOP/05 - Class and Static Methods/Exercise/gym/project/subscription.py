from project import AutoIncrementMixin


class Subscription(AutoIncrementMixin):
    def __init__(
        self, date: str, customer_id: int, trainer_id: int, exercise_id: int
    ) -> None:

        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.get_next_id()

    def __repr__(self) -> str:
        return f"Subscription <{self.id}> on {self.date}"
