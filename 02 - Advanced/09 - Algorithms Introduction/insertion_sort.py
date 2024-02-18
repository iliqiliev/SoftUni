from typing import List


def insertion_sort(items: List[int]) -> List[int]:
    length = len(items)

    for start in range(1, length):
        for index in range(start, 0, -1):
            if items[index - 1] > items[index]:
                items[index], items[index - 1] = items[index - 1], items[index]

            else:
                break

    return items


def main():
    items = list(map(int, input().split()))

    sorted_sequence = insertion_sort(items)

    print(*sorted_sequence)


if __name__ == "__main__":
    main()
