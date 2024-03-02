from collections import defaultdict
from typing import Dict, Union


class PizzaDelivery:
    def __init__(
        self, name: str, price: float, ingredients: Dict[str, int]
    ) -> None:

        self.name = name
        self.price = price
        self.ingredients = defaultdict(int, ingredients)
        self.ordered = False

    def add_extra(
        self, ingredient: str, units: int, unit_price: float
    ) -> Union[str, None]:

        if self.ordered:
            return self.already_ordered()

        self.ingredients[ingredient] += units
        self.price += units * unit_price

        return None

    def remove_ingredient(
        self, ingredient: str, units: int, unit_price: float
    ) -> Union[str, None]:

        if self.ordered:
            return self.already_ordered()

        if ingredient not in self.ingredients:
            return (
                f"Wrong ingredient selected! "
                f"We do not use {ingredient} in {self.name}!"
            )

        if units > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= units
        self.price -= units * unit_price

        return None  # :(

    def make_order(self) -> str:
        self.ordered = True

        ingredients = ", ".join(
            f"{ingredient}: {quantity}"
            for ingredient, quantity in self.ingredients.items()
        )

        return (
            f"You've ordered pizza {self.name} prepared with {ingredients} "
            f"and the price will be {self.price}lv."
        )

    def already_ordered(self) -> str:
        return f"Pizza {self.name} already prepared, and we can't make any changes!"
