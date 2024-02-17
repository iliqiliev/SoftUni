def sorting_cheeses(**cheeses: list) -> str:
    sorted_cheeses = ""

    for cheese, quantities in sorted(cheeses.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        sorted_cheeses += f"{cheese}\n"

        for quantity in sorted(quantities, reverse=True):
            sorted_cheeses += f"{quantity}\n"

    return sorted_cheeses
