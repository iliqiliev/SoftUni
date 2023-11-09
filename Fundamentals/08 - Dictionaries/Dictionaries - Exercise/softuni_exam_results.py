from collections import defaultdict


students = defaultdict(list)
submissions_count = defaultdict(int)

while True:
    command = input().split("-")
    if command[0] == "exam finished":
        break

    if len(command) == 2:
        name = command[0]
        students[name] = [-1] * len(students[name])

    elif len(command) == 3:
        name, programming_language, score = command
        score = int(score)

        students[name].append(score)
        submissions_count[programming_language] += 1

print("Results:")
for student, scores in students.items():
    # don't show banned people
    if -1 not in scores:
        print(f"{student} | {max(scores)}")

print("Submissions:")
for language, count in submissions_count.items():
    print(f"{language} - {count}")
