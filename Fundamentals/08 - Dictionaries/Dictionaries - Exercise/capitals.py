countries = input().split(", ")
capitals = input().split(", ")

countries_with_capitals = {countries[i]: capitals[i] for i in range(len(countries))}

for country, capital in countries_with_capitals.items():
    print(f"{country} -> {capital}")
