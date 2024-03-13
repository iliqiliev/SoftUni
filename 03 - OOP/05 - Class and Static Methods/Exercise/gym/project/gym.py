from typing import List, TypeVar
from project import Customer, Equipment, ExercisePlan, Subscription, Trainer


Item = TypeVar("Item", Customer, Equipment, ExercisePlan, Subscription, Trainer)


class Gym:
    def __init__(self) -> None:
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    @staticmethod
    def _add_item(item: Item, items: List[Item]) -> None:
        if item not in items:
            items.append(item)

    def add_customer(self, customer: Customer) -> None:
        self._add_item(customer, self.customers)

    def add_trainer(self, trainer: Trainer) -> None:
        self._add_item(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment) -> None:
        self._add_item(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        self._add_item(plan, self.plans)

    def add_subscription(self, subscriptions: Subscription) -> None:
        self._add_item(subscriptions, self.subscriptions)

    @staticmethod
    def _get_item(item_id: int, items: List[Item]) -> Item:
        try:
            return next(item for item in items if item.id == item_id)

        except StopIteration as error:
            raise LookupError from error

    def subscription_info(self, subscription_id: int) -> str:
        subscriptions = self._get_item(subscription_id, self.subscriptions)

        customer = self._get_item(subscriptions.customer_id, self.customers)
        trainer = self._get_item(subscriptions.trainer_id, self.trainers)
        plan = self._get_item(subscriptions.exercise_id, self.plans)
        equipment = self._get_item(plan.equipment_id, self.equipment)

        return "\n".join(
            str(item) for item in
            (subscriptions, customer, trainer, equipment, plan)
        )
