from typing import List, Tuple


DIRECTIONS = {
    "up":    (-1, 0),
    "down":  (+1, 0),
    "left":  (0, -1),
    "right": (0, +1),
}


def in_neighbourhood(boy: Tuple[int, int], rows: int, cols: int) -> bool:
    return 0 <= boy[0] < rows and 0 <= boy[1] < cols


def move(
    neighbourhood: List[List[str]],
    boy: Tuple[int, int],
    direction: str,
    rows: int, cols: int
) -> Tuple[int, int]:

    delta = DIRECTIONS[direction]

    new_boy = (
        boy[0] + delta[0],
        boy[1] + delta[1]
    )

    if not in_neighbourhood(new_boy, rows, cols):
        raise IndexError("Boy exited neighbourhood")

    if neighbourhood[new_boy[0]][new_boy[1]] == "*":
        return boy

    return new_boy


def print_matrix(matrix: List[List[str]]) -> None:
    for row in matrix:
        print("".join(row))


def main():
    rows, cols = map(int, input().split())

    matrix = []
    boy = (0, 0)

    for row_index in range(rows):
        row_data = list(input())

        if "B" in row_data:
            col_index = row_data.index("B")
            boy = (row_index, col_index)

        matrix.append(row_data)

    initial_boy = boy

    while True:
        try:
            boy = move(matrix, boy, input(), rows, cols)

        except IndexError:
            print("The delivery is late. Order is canceled.")

            matrix[initial_boy[0]][initial_boy[1]] = " "
            break

        position_data = matrix[boy[0]][boy[1]]

        if position_data == "-":
            matrix[boy[0]][boy[1]] = "."

        elif position_data == "P":  # the time/turns are not counted
            print("Pizza is collected. 10 minutes for delivery.")

            matrix[boy[0]][boy[1]] = "R"

        elif position_data == "A":  # the input always collects pizza
            print("Pizza is delivered on time! Next order...")

            matrix[boy[0]][boy[1]] = "P"
            break

    print_matrix(matrix)


if __name__ == "__main__":
    main()
