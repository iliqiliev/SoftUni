from collections import defaultdict
from functools import partial


def dwarf_sorting(dwarf_info: tuple, all_dwarfs: dict) -> tuple:
    # example dwarf_info ('Red Grumpy', 10000)
    hat_colour_with_name, score = dwarf_info
    hat_colour = hat_colour_with_name.split()[0]

    # count the dwarfs with the same colour; example key - 'Red Grumpy'
    hat_count = sum(1 for key in all_dwarfs.keys() if key.startswith(hat_colour))

    # sort both in descending order
    return (-score, -hat_count)


dwarfs = defaultdict(int)

while True:
    command = input().split(" <:> ")
    if len(command) == 1:
        break

    name, colour, physics = command
    physics = int(physics)

    # The key is the colour and it stores all dwarfs with that colour.
    # The physics for each dwarf is the biggest given
    dwarfs[f"{colour} {name}"] = max(physics, dwarfs.get((f"{colour} {name}"), 0))

# The partial function is dwarf_sorting with all_dwarfs already set to dwarfs.
# This is because you can't put function parameters in key=
sort_current_dwarfs = partial(dwarf_sorting, all_dwarfs=dwarfs)

for colour_name, physics in sorted(dwarfs.items(), key=sort_current_dwarfs):
    colour, name = colour_name.split()
    print(f"({colour}) {name} <-> {physics}")
