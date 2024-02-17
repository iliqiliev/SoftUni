def clamp(value, floor: int, ceiling: int):
    return max(min(ceiling, value), floor)


def merge(starting_index: int, ending_index: int, strings: list) -> list:

    # clamp indexes between 0 and the biggest valid index
    starting_index = clamp(starting_index, 0, len(strings) - 1)
    ending_index = clamp(ending_index, 0, len(strings) - 1)

    # replace the element with a string that is the concatenated
    # elements from the starting index to the ending index
    strings[starting_index] = "".join(strings[starting_index:ending_index + 1])

    # delete the elements we have merged but not the first because
    # have replaced him with the merged one
    del strings[starting_index + 1: ending_index + 1]

    return strings


def divide(index: int, partitions: int, strings: list) -> list:

    divided_element = list()
    element = strings[index]

    length = len(strings[index])
    size, remainder = divmod(length, partitions)

    # (length - remainder) to avoid creating a partition that is smaller than the others
    for part in range(0, length - remainder, size):
        divided_element.append(element[part: part + size])
    if remainder:  # if there is a remainder add it to the last element as required
        divided_element[-1] += element[-remainder:]

    # this is the correct syntax for replacing the divided element with the partitions
    strings[index:index + 1] = divided_element

    return strings


strings = input().split()

command = input().split()
while command[0] != "3:1":

    command, index, option = command[0], int(command[1]), int(command[2])

    if command == "merge":
        merge(index, option, strings)
    elif command == "divide":
        divide(index, option, strings)

    command = input().split()

print(*strings)
