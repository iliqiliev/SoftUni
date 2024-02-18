from typing import Sequence


def binary_search_number(sequence: Sequence[int], target: int) -> int:
    start = 0
    end = len(sequence) - 1

    while start <= end:
        middle = (end + start) // 2
        middle_element = sequence[middle]

        if middle_element == target:
            return middle

        if middle_element < target:
            start = middle + 1

        else:
            end = middle - 1

    return -1


def main():
    sequence = list(map(int, input().split()))
    target = int(input())

    index = binary_search_number(sequence, target)

    print(index)


if __name__ == "__main__":
    main()
