from collections import defaultdict
from typing import Tuple


def accommodate_new_pets(
    capacity: int,
    max_pet_weight: float,
    *pets: Tuple[str, float]
) -> str:

    accommodated = defaultdict(int)

    for pet_type, pet_weight in pets:
        if not capacity:
            status = "You did not manage to accommodate all pets!"
            break

        if pet_weight > max_pet_weight:
            continue

        accommodated[pet_type] += 1
        capacity -= 1

    else:
        status = f"All pets are accommodated! Available capacity: {capacity}."

    formatted_status = [
        status,
        "Accommodated pets:",
        *(f"{pet}: {count}" for pet, count in sorted(accommodated.items()))
    ]

    return "\n".join(formatted_status)
