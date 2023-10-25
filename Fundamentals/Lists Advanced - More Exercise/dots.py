def main():

    rows = int(input())
    board = []

    for row in range(rows):
        board.append(input().split())

    print(board_dots_max(board))


def current_dot_sum(board: list, row=0, col=0, ) -> int:

    if (not row in range(0, len(board))) or \
       (not col in range(0, len(board[0]))) or \
       board[row][col] == "-":
        # check if the current element is a dash
        # or the index is invalid (occurs in the recursive searches)
        return 0

    max_dots = 1 # we have a dot
    board[row][col] = "-" # replace the dot with a dash to avoid counting it again

    # checking the cardinal directions for neighboring dots
    max_dots += current_dot_sum(board, row - 1, col)  # top
    max_dots += current_dot_sum(board, row + 1, col)  # bottom
    max_dots += current_dot_sum(board, row, col - 1)  # left
    max_dots += current_dot_sum(board, row, col + 1)  # right
    
    return max_dots

def board_dots_max(board: list) -> int:

    dots_max = 0
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == ".":
                dots_max = max(dots_max, current_dot_sum(board, row, col))
                
    return dots_max

if __name__ == "__main__":
    main()
