import os


SIZE = 3
TOTAL_CELLS = SIZE ** 2


def clear_screen() -> None:
    terminal_lines = os.get_terminal_size()[1]
    print("\n" * (terminal_lines))


def print_board(board=None) -> None:
    def print_line():
        if board:
            element = board[index - 1]

        else:
            element = index

        str_len = len(str(element))
        # works up to SIZE 31
        print(f"{' ' * (str_len < 2)}{element}{' ' * (str_len < 3)}|", end="")

    horizontal_line = "+" + "---+" * SIZE
    index = 1

    for _ in range(SIZE):
        print(f"{horizontal_line}\n|", end="")

        for _ in range(SIZE):
            print_line()
            index += 1

        print()

    print(horizontal_line)


def place_symbol(board: list[str], player: str, symbol: str) -> bool:
    try:
        position = int(input(f"{player}, please enter position: ")) - 1

    except ValueError:
        return False

    if position not in range(TOTAL_CELLS) or board[position] != " ":
        return False

    board[position] = symbol
    return True


def check_winner(
    board: list[str], turn: int, symbol: str, winning_combinations: list[list[int]]
) -> bool:
    if turn < SIZE * 2 - 1:
        return False

    for combination in winning_combinations:
        if all(board[index] == symbol for index in combination):
            return True

    return False


def generate_winning_combinations() -> list[list[int]]:
    rows = [[row * SIZE + col for col in range(SIZE)] for row in range(SIZE)]

    cols = [[row * SIZE + col for row in range(SIZE)] for col in range(SIZE)]

    diagonals = [
        [index * SIZE + index for index in range(SIZE)],     # main
        [(index + 1) * (SIZE - 1) for index in range(SIZE)]  # secondary
    ]

    return rows + cols + diagonals


def refresh_screen(board=None) -> None:
    clear_screen()
    print_board(board=board)


def mainloop(players: list[str]):
    turn = 0
    symbols = "XO"
    board = [" "] * TOTAL_CELLS

    player = None
    symbol = symbols[0]

    winning_combinations = generate_winning_combinations()

    while True:
        refresh_screen(board)

        if check_winner(board, turn, symbol, winning_combinations):
            print(f"{player} won!")
            break

        if turn == TOTAL_CELLS:
            print("Draw!")
            break

        symbol = symbols[turn % 2]
        player = players[turn % 2]

        if not place_symbol(board, player, symbol):
            input("Please select empty cell inside the board. Enter to continue: ")
            continue

        turn += 1


def main():
    clear_screen()

    while len(players := input(
        "Enter names for the two players separated by a comma: "
    ).split(", ")) != 2:
        print("Enter two names!")

    refresh_screen()
    input("Enter positions according to the table. Enter to continue: ")

    mainloop(players)


if __name__ == "__main__":
    main()
