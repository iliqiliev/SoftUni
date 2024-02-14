from collections import deque


initial_fuel = list(map(int, input().split()))
additional_consumption = deque(map(int, input().split()))
altitude_fuel_requirements = map(int, input().split())


for index, requirement in enumerate(altitude_fuel_requirements, start=1):
    current_reach = initial_fuel.pop() - additional_consumption.popleft()

    if current_reach >= requirement:
        print(f"John has reached: Altitude {index}")

    else:
        reached = (
            "Reached altitudes: "
            f"{', '.join(f'Altitude {level}' for level in range(1, index))}"
        )
        print(
            f"John did not reach: Altitude {index}",
            "John failed to reach the top.",
            "John didn't reach any altitude." if index == 1 else reached,
            sep="\n"
        )
        break

else:
    print("John has reached all the altitudes and managed to reach the top!")
