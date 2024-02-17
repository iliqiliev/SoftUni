def add_stop(stops: str, index: int, string: str) -> str:
    if 0 <= index < len(stops):
        stops = stops[:index] + string + stops[index:]

    return stops


def remove_stop(stops: str, start_index: int, end_index: int) -> str:
    if all(0 <= index < len(stops) for index in (start_index, end_index)):
        stops = stops[:start_index] + stops[end_index + 1:]

    return stops


def switch_stop(stops: str, old_string: str, new_string: str) -> str:
    return stops.replace(old_string, new_string)


def main():
    stops = input()

    commands = {
        "Add Stop": add_stop,
        "Remove Stop": remove_stop,
        "Switch": switch_stop,
    }

    while True:
        command, *arguments = input().split(":")
        if command not in commands:
            break

        arguments = [int(arg) if arg.isdigit() else arg for arg in arguments]
        stops = commands[command](stops, *arguments)
        print(stops)

    print(f"Ready for world tour! Planned stops: {stops}")


if __name__ == "__main__":
    main()
