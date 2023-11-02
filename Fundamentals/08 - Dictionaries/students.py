students = {}

command = input().split(":")
while len(command) == 3:
    name, student_id, course = command
    students[student_id] = (name, course)

    command = input().split(":")

command = command[0].replace("_", " ")
for student_id, (name, course) in students.items():
    if course == command:
        print(f"{name} - {student_id}")
