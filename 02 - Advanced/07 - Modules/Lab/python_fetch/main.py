from pyfiglet import figlet_format
from termcolor import colored, COLORS

from python_fetch.core import generate_system_info


colours = tuple(colour for colour in COLORS if "_" not in colour)

while (colour := input("Enter colour: ").lower()) not in colours:
    print(f"Please select any of these colours: {', '.join(colours)}!")


logo = figlet_format("PythonFetch")
print(colored(text=logo, color=colour))

for stat, value in generate_system_info().items():
    print(colored(text=f"{stat}: {value}", color=colour))
