def modify_set(command: str, set_name: str, sequence: set) -> None:
    if command == "Add":
        sets[set_name].update(sequence)

    elif command == "Remove":
        sets[set_name].difference_update(sequence)


def check_subset() -> bool:
    return (sets["First"] <= sets["Second"] or sets["Second"] <= sets["First"])


sets = {
    "First":  {int(num) for num in input().split()},
    "Second": {int(num) for num in input().split()},
}


def main():
    for _ in range(int(input())):
        command, set_name, *sequence = input().split()
        if sequence:
            sequence = {int(num) for num in sequence}
            modify_set(command, set_name, sequence)

        else:
            print(check_subset())

    print(*sorted(sets["First"]), sep=", ")
    print(*sorted(sets["Second"]), sep=", ")


if __name__ == "__main__":
    main()
