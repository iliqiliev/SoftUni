from collections import defaultdict


courses = defaultdict(list)

while True:
    command = input()
    if command == "end":
        break

    course, name = command.split(" : ")
    courses[course].append(name)

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
