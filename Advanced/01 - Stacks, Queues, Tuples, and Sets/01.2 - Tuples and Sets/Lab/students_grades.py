from collections import defaultdict


students = defaultdict(list)

for _ in range(int(input())):
    name, grade = input().split()
    students[name].append(float(grade))

for name, grades in students.items():
    formatted_grades = " ".join(f"{grade:.2f}" for grade in grades)
    print(f"{name} -> {formatted_grades} (avg: {sum(grades) / len(grades):.2f})")
