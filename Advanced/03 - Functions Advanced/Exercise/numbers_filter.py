from typing import List, Dict


def even_odd_filter(**numbers: List[int]) -> Dict[str, List[int]]:
    if "even" in numbers:
        numbers["even"] = [num for num in numbers["even"] if not num & 1]

    if "odd" in numbers:
        numbers["odd"] = [num for num in numbers["odd"] if num & 1]

    return dict(sorted(numbers.items(), key=lambda kvp: -len(kvp[1])))
