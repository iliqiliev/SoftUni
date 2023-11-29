def drive(cars: dict, car: str, distance: int, fuel: int) -> dict:
    if cars[car]["fuel"] >= fuel:
        cars[car]["fuel"] -= fuel
        cars[car]["mileage"] += distance

        print(
            f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
        )

    else:
        print("Not enough fuel to make that ride")

    if cars[car]["mileage"] >= 100000:
        print(f"Time to sell the {car}!")
        cars.pop(car)

    return cars


def refuel(cars: dict, car: str, fuel: int) -> dict:
    refill = min(75 - cars[car]["fuel"], fuel)
    cars[car]["fuel"] += refill
    print(f"{car} refueled with {refill} liters")

    return cars


def revert(cars: dict, car: str, kilometres: int) -> dict:
    cars[car]["mileage"] -= kilometres

    if cars[car]["mileage"] < 10000:
        cars[car]["mileage"] = 10000
        return cars

    print(f"{car} mileage decreased by {kilometres} kilometers")
    return cars


def main():
    cars = {}

    for _ in range(int(input())):
        car_model, mileage, fuel = input().split("|")

        cars[car_model] = {"mileage": int(mileage), "fuel": int(fuel)}

    commands = {
        "Drive": drive,
        "Refuel": refuel,
        "Revert": revert,
    }

    while True:
        command, *arguments = input().split(" : ")
        if command not in commands:
            break

        arguments = [int(arg) if arg.isdigit() else arg for arg in arguments]
        cars = commands[command](cars, *arguments)

    for car_name, car_info in cars.items():
        print(
            f"{car_name} -> Mileage: {car_info['mileage']} kms, "
            f"Fuel in the tank: {car_info['fuel']} lt."
        )


if __name__ == "__main__":
    main()
