from collections import defaultdict


students = defaultdict(list)
number_of_students = int(input())

for student in range(number_of_students):
    name, grade = input(), float(input())

    students[name].append(grade)

for name, grade in students.items():
    average_grade = sum(grade) / len(grade)

    if average_grade >= 4.5:
        print(f"{name} -> {average_grade:.2f}")
