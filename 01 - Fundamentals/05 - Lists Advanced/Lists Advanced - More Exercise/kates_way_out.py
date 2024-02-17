def main():

    maze_size = int(input())
    maze = []
    kate_index = []

    for line in range(maze_size):
        maze.append(list(input()))

        if "k" in maze[line]:
            kate_index = [line, maze[line].index("k")]

    moves = escape_maze(kate_index[0], kate_index[1], maze)

    if not moves:
        print("Kate cannot get out")
    else:
        print(f"Kate got out in {moves} moves")


def escape_maze(row: int, col: int, maze: list, moves=0) -> int:
    # if kate has reached a border region return the moves until now
    if not (0 <= row < len(maze) and 0 <= col < len(maze[0])):
        return moves

    # if kate has reached a dead end return 0 (cannot escape)
    if maze[row][col] == "#":
        return 0

    # set her position to # to avoid going back
    maze[row][col] = "#"

    # recursively look at all different paths
    result_top = escape_maze(row - 1, col, maze, moves + 1)
    result_bottom = escape_maze(row + 1, col, maze, moves + 1)
    result_left = escape_maze(row, col - 1, maze, moves + 1)
    result_right = escape_maze(row, col + 1, maze, moves + 1)

    # we are looking for the longest path so we compare them all
    return max(result_top, result_bottom, result_right, result_left)


if __name__ == "__main__":
    main()
