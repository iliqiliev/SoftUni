population_wealth = [int(wealth) for wealth in input().split(", ")]
minimum_wealth = int(input())

while min(population_wealth) < minimum_wealth:

    poorest = min(population_wealth)
    richest = max(population_wealth)

    poorest_index = population_wealth.index(poorest)
    richest_index = population_wealth.index(richest)

    if ((richest - minimum_wealth) - (minimum_wealth - poorest)) >= 0:
        population_wealth[richest_index] -= minimum_wealth - poorest
        population_wealth[poorest_index] += minimum_wealth - poorest

    else:
        print("No equal distribution possible")
        break

else:
    print(population_wealth)
