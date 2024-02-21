from itertools import chain


def draw_rhombus(size: int) -> None:
    top_part = range(1, size + 1)
    bottom_part = range(size - 1, 0, -1)

    for row_index in chain(top_part, bottom_part):
        print(" " * (size - row_index), "* " * row_index, sep="")


def main():
    size = int(input())

    draw_rhombus(size)


if __name__ == "__main__":
    main()
