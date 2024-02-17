from collections import defaultdict
from typing import List, Tuple


def cookbook(*dishes_info: Tuple[str, str, List[str]]) -> str:
    recipes = defaultdict(list)

    for dish, origin, ingredients in dishes_info:
        recipes[origin].append((dish, ingredients))

    sorted_recipes = sorted(
        recipes.items(),
        key=lambda kvp: (-len(kvp[1]), kvp[0])
    )

    result = []

    for origin, recipes in sorted_recipes:
        result.append(f"{origin} cuisine contains {len(recipes)} recipes:")

        for dish, ingredients in sorted(recipes):
            result.append(f"  * {dish} -> Ingredients: {', '.join(ingredients)}")

    return "\n".join(result)
