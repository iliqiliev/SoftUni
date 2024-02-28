from typing import List
from project import Pokemon


class Trainer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        for pokemon in self.pokemons:
            if pokemon_name == pokemon.name:
                self.pokemons.remove(pokemon)

                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        data = [
            f"Pokemon Trainer {self.name}",
            f"Pokemon count {len(self.pokemons)}",
            *(f"- {pokemon.pokemon_details()}" for pokemon in self.pokemons)
        ]

        return "\n".join(data)
