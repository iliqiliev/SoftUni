def scream_input(command: str) -> list:
    instructions = []
    current_number = ""
    current_word = ""

    for char in command:
        if char.isdigit():
            # check if there is a word
            if current_word:
                # append it to the list and reset it
                instructions.append(current_word)
                current_word = ""

            # add the digit to the current digit
            current_number += char

        else:
            # mirrored
            if current_number:
                instructions.append(int(current_number))
                current_number = ""

            current_word += char

    # the number is always last and nothing adds it otherwise
    instructions.append(int(current_number))

    return instructions


def scream(instructions: list) -> str:
    gamer_scream = ""
    unique_symbols = ""

    for index in range(0, len(instructions), 2):
        string = instructions[index].upper()
        repeats = instructions[index + 1]

        # add the string to a set so it stores only the unique symbols
        unique_symbols += string
        gamer_scream += string * repeats

    return f"Unique symbols used: {len(set(unique_symbols))}\n{gamer_scream}"


def main():
    command = scream_input(input())

    print(scream(command))


if __name__ == "__main__":
    main()
