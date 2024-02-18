from typing import List, Set


def set_cover(universe: Set[int], subsets: List[Set[int]]) -> List[Set[int]]:
    taken_subsets = []

    for _ in range(len(subsets)):
        best_set = max(subsets, key=lambda subset: len(universe.intersection(subset)))

        if not universe.intersection(best_set):
            break

        universe.difference_update(best_set)
        taken_subsets.append(best_set)

        if not universe:
            return taken_subsets

    raise ValueError("No solution exists")


def main():
    universe = set(map(int, input().split(", ")))
    subsets = [
        set(map(int, input().split(", ")))
        for _ in range(int(input()))
    ]

    try:
        chosen_sets = set_cover(universe, subsets)

    except ValueError as error:
        print(error)
        return

    print(
        f"Sets to take ({len(chosen_sets)}):",
        *(f"\n{{ {', '.join(map(str, sorted(subset)))} }}" for subset in chosen_sets),
        sep=""
    )


if __name__ == "__main__":
    main()
