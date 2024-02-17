def key_error_message(key, dictionary: dict) -> None:
    print(f"{key} does not exist in dictionary.\n"
          f"Valid numbers: {' '.join(dictionary)}")


def main():
    numbers_dictionary = {}

    while (number_word := input()) != "Search":  # Adding
        try:
            numbers_dictionary[number_word] = int(input())

        except ValueError:
            print("Please enter integers only.")

    while (searched := input()) != "Remove":  # Searching
        try:
            print(numbers_dictionary[searched])

        except KeyError:
            key_error_message(searched, numbers_dictionary)

    while (target := input()) != "End":  # Removing
        try:
            del numbers_dictionary[target]

        except KeyError:
            key_error_message(target, numbers_dictionary)

    print(numbers_dictionary)


if __name__ == "__main__":
    main()
