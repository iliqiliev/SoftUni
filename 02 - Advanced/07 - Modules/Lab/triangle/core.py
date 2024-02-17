def create_triangle(size: int) -> None:
    def print_row():
        print(*range(1, row_index + 1))

    for row_index in range(1, size + 1):
        print_row()

    for row_index in range(size - 1, 0, -1):
        print_row()
