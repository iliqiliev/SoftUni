number_of_commands = int(input())
parking_lot = {}

for command in range(number_of_commands):
    command = input().split()

    if command[0] == "register":
        name, license_plate = command[1:]

        if name in parking_lot:
            print(f"ERROR: already registered with plate number {parking_lot[name]}")

        else:
            parking_lot[name] = license_plate
            print(f"{name} registered {license_plate} successfully")

    elif command[0] == "unregister":
        name = command[1]

        if name in parking_lot:
            parking_lot.pop(name)
            print(f"{name} unregistered successfully")

        else:
            print(f"ERROR: user {name} not found")

for name, plate in parking_lot.items():
    print(f"{name} => {plate}")
