import os


class FullColumnError(Exception):
    pass


ROWS = 6
COLS = 7
CONNECT_TARGET = 4

DIRECTIONS = (
    (0,  -1),  # horizontal
    (-1, -1),  # main diagonal
    (-1,  0),  # vertical
    (-1,  1),  # anti-diagonal
)


def clear_screen() -> None:
    terminal_lines = os.get_terminal_size()[1]
    print("\n" * (terminal_lines - ROWS - 1))


def create_board(rows: int, cols: int) -> list[list[int]]:
    return [[0] * cols for _ in range(rows)]


def print_board(board: list[list[int]]) -> None:
    for row in board:
        print(row)


def check_winner(board: list[list[int]], move: (tuple[int, int] | None)) -> bool:
    if move is None:
        return False

    def travel_board(travel_direction=1) -> int:
        player_token = board[move[0]][move[1]]
        equal_cells = 0

        for delta in range(1, CONNECT_TARGET):
            cell_x = move[0] + (direction[0] * travel_direction * delta)
            cell_y = move[1] + (direction[1] * travel_direction * delta)

            try:
                check_in_board((cell_x, cell_y))

            except IndexError:
                break

            if board[cell_x][cell_y] != player_token:
                break

            equal_cells += 1

        return equal_cells

    for direction in DIRECTIONS:
        player_connected = travel_board() + travel_board(travel_direction=-1)

        if player_connected + 1 >= CONNECT_TARGET:
            return True

    return False


def check_in_board(move: tuple[int, int]) -> None:
    if not (0 <= move[0] < ROWS and 0 <= move[1] < COLS):
        raise IndexError("Outside of game board")


def place_on_board(
    board: list[list[int]], player: int, col_index: int
) -> tuple[int, int]:

    check_in_board((0, col_index))

    for row_index in range(ROWS - 1, -1, -1):
        if not board[row_index][col_index]:
            board[row_index][col_index] = player
            return (row_index, col_index)

    raise FullColumnError


def refresh_screen(board: list[list[int]]) -> None:
    clear_screen()
    print_board(board)


def mainloop(board: list[list[int]]) -> None:
    turn = 0
    player = None
    move = None

    while True:
        refresh_screen(board)

        if check_winner(board, move):
            print(f"Player {player} won!")
            break

        if turn >= ROWS * COLS:
            print(("Board is full. Draw!"))
            break

        player = (turn % 2) + 1

        try:
            player_move = int(input(f"Player {player} enter column: ")) - 1
            move = place_on_board(board, player, player_move)

        except FullColumnError:
            print("Column is full!")

        except (IndexError, ValueError):
            print(f"Invalid column. Please enter column from 1 to {COLS}!")

        except KeyboardInterrupt:
            print("\nExiting game!")
            break

        else:
            turn += 1
            continue

        input("Enter to continue: ")


def main():
    board = create_board(ROWS, COLS)

    clear_screen()
    mainloop(board)


if __name__ == "__main__":
    main()
