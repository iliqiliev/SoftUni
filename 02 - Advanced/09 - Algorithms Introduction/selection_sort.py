from typing import List


def selection_sort(items: List[int]) -> List[int]:
    length = len(items)

    for index in range(length - 1):
        min_index = index

        for try_index in range(index + 1, length):
            if items[try_index] < items[min_index]:
                min_index = try_index

        items[min_index], items[index] = items[index], items[min_index]

    return items


def main():
    items = list(map(int, input().split()))

    sorted_sequence = selection_sort(items)

    print(*sorted_sequence)


if __name__ == "__main__":
    main()
