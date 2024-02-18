def recursive_drawing(size: int) -> None:
    if not size:
        return

    print("*" * size)

    recursive_drawing(size - 1)

    print("#" * size)

    return


def main():
    recursive_drawing(int(input()))


if __name__ == "__main__":
    main()
