class Zoo:
    __animals = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.animals = {"mammal": [], "fish": [], "bird": []}

    def add_animal(self, species: str, name: str) -> None:
        self.animals[species].append(name)

        Zoo.__animals += 1

    def get_info(self, species: str) -> str:
        animals_names = ", ".join(self.animals[species])
        # only the plural of fish ends with "es"
        verb_ending = "es" if species == "fish" else "s"

        return (f"{species.capitalize()}{verb_ending} in {self.name}: {animals_names}\n"
                f"Total animals: {Zoo.__animals}")


# create a Zoo object and read the zoo's name from the user
zoo = Zoo(input())

for animal in range(int(input())):
    # unpack the users input and use it as arguments for the add_animal method
    zoo.add_animal(*input().split())

# get info for required animal biological class (not Python class)
print(zoo.get_info(input()))
