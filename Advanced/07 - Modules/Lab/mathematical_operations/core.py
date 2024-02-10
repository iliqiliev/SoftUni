from math import sqrt


def perfect_square(x: int) -> bool:
    root = sqrt(x)
    return root == int(root)


def fibonacci_index(number: int, sequence: list[int]) -> int:
    base = 5 * number ** 2  # 🤓
    if not (perfect_square(base + 4) or perfect_square(base - 4)):
        return 0

    try:
        return sequence.index(number)

    except ValueError:
        return 0


def generate_fibonacci(length: int) -> list[int]:
    sequence = [0, 1]

    for _ in range(length - 2):
        sequence.append(sequence[-2] + sequence[-1])

    return sequence
