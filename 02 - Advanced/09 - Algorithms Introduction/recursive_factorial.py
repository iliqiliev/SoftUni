def recursive_factorial(number: int) -> int:
    if number > 1:
        return number * recursive_factorial(number - 1)

    return 1


def main():
    print(recursive_factorial(int(input())))


if __name__ == "__main__":
    main()
