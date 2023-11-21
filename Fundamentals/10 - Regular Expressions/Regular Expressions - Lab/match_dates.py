import re


date_pattern = (
    r"\b(?P<day>\d{2})(?P<sep>[-\/.])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})"
)

for match in re.finditer(date_pattern, input()):
    print(f"Day: {match['day']}, Month: {match['month']}, Year: {match['year']}")
