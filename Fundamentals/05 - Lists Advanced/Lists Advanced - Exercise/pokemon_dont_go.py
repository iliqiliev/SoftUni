def pokemon_distance(pokemons: list, removed_value: int) -> list:

    for index, pokemon in enumerate(pokemons):
        if pokemon <= removed_value:
            pokemons[index] += removed_value

        else:
            pokemons[index] -= removed_value

    return pokemons


def pokemon_catch(pokemons: list, index: int, pokemon_score: int) -> int:

    if index < 0:
        removed_pokemon = pokemons[0]
        pokemons[0] = pokemons[-1]

    elif index > len(pokemons) - 1:
        removed_pokemon = pokemons[-1]
        pokemons[-1] = pokemons[-0]

    else:
        removed_pokemon = pokemons.pop(index)

    pokemon_distance(pokemons, removed_pokemon)
    pokemon_score += removed_pokemon

    return pokemon_score


pokemons = [int(number) for number in input().split()]
pokemon_score = 0

while pokemons:
    index = int(input())
    pokemon_score = pokemon_catch(pokemons, index, pokemon_score)

print(pokemon_score)
