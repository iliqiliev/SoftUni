from typing import List


def bubble_sort(items: List[int]) -> List[int]:
    repeats = len(items) - 1

    for repeat in range(repeats):
        for index in range(repeats - repeat):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]

    return items


def main():
    items = list(map(int, input().split()))

    sorted_sequence = bubble_sort(items)

    print(*sorted_sequence)


if __name__ == "__main__":
    main()
