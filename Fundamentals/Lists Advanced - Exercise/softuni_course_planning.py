def course_planner(command_as_str: str, curriculum: list) -> None:
    """
    Performs operations on a curriculum list.
    Treat every subject as a list consisting of the subject name
    and a bool that is true if the subject has exercise.
    """

    command, lesson_title, *third_option = command_as_str.split(":")
    # avoid error if there are only two values(every case except swap and insert)
    if third_option:
        third_option = third_option[0]

    curriculum_subjects = [name[0] for name in curriculum]

    if lesson_title not in curriculum_subjects:
        if command == "Add":
            curriculum.append([lesson_title, False])

        elif command == "Insert":
            index = int(third_option)  # type: ignore (vscode)
            curriculum.insert(index, [lesson_title, False])

    else:
        if command == "Remove":
            index = curriculum_subjects.index(lesson_title)
            curriculum.pop(index)

        elif command == "Swap" and third_option in curriculum_subjects:
            first_index = curriculum_subjects.index(lesson_title)
            second_index = curriculum_subjects.index(third_option)

            curriculum[first_index], curriculum[second_index] = (
                curriculum[second_index], curriculum[first_index])

    if command == "Exercise":
        if lesson_title not in curriculum_subjects:
            curriculum.append([lesson_title, True])

        else:
            index = curriculum_subjects.index(lesson_title)
            curriculum[index][1] = True


def course_formatting(curriculum: list) -> list:
    """
    Put the exercises in the curriculum and 
    remove the entries for subjects with no exercise.
    """
    new_curriculum = list()

    for pair in curriculum:
        if pair[1]:
            pair[1] = f"{pair[0]}-Exercise"

        for element in pair:
            if element:
                new_curriculum.append(element)

    for index, subject in enumerate(new_curriculum, 1):
        print(f"{index}.{subject}")

    return new_curriculum


curriculum = [[subject, False] for subject in input().split(", ")]

command = input()
while command != "course start":

    course_planner(command, curriculum)

    command = input()

curriculum = course_formatting(curriculum)
