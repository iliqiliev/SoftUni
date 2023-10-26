number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

students = [int(input()) for attendance in range(number_of_students)]

# avoid error when the number of students is 0
max_student_attendance = max(students) if students else 0
# same thing if the number of lectures is 0
max_student_bonus = (max_student_attendance / number_of_lectures) * \
    (5 + additional_bonus) if number_of_lectures else 0

# makeshift Math.ceil
print(f"Max Bonus: {-int(-max_student_bonus)}.\n"
      f"The student has attended {max_student_attendance} lectures.")
