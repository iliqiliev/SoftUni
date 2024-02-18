from typing import List


def recursive_sum(array: List[int]) -> int:
    if len(array) > 1:
        return array.pop() + recursive_sum(array)

    if array:
        return array.pop()

    return 0


def main():
    array = list(map(int, input().split()))

    print(recursive_sum(array))


if __name__ == "__main__":
    main()
