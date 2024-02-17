# nearly a copy/paste from courses.py
from collections import defaultdict


companies = defaultdict(list)

while True:
    command = input()
    if command == "End":
        break

    company, employee_id = command.split(" -> ")

    if employee_id not in companies[company]:
        companies[company].append(employee_id)

for company, employees in companies.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
