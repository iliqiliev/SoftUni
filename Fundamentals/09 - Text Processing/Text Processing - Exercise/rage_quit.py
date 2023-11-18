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

    for index in range(0, len(instructions), 2):
        string = instructions[index].upper()
        repeats = instructions[index + 1]

        gamer_scream += string * repeats

    return f"Unique symbols used: {len(set(gamer_scream))}\n{gamer_scream}"


def main():
    instructions = scream_input(input())

    print(scream(instructions))


if __name__ == "__main__":
    main()
