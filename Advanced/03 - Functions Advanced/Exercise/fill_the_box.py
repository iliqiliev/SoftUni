def fill_the_box(x: int, y: int, z: int, *args: int and str) -> str:
    box_size = x * y * z
    cubes = sum(args[: args.index("Finish")])

    box_size -= cubes

    if box_size > 0:
        return ("There is free space in the box. "
                f"You could put {box_size} more cubes.")

    return f"No more free space! You have {-box_size} more cubes."
