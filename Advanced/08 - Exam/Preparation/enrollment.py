from typing import Tuple


def gather_credits(credit_needed: int, *courses: Tuple[str, int]) -> str:
    credit_gathered = 0
    courses_enrolled = set()

    for name, credit_given in courses:
        if name in courses_enrolled:
            continue

        if credit_gathered >= credit_needed:
            break

        credit_gathered += credit_given
        courses_enrolled.add(name)

    if credit_gathered >= credit_needed:
        return (
            f"Enrollment finished! Maximum credits: {credit_gathered}.\n"
            f"Courses: {', '.join(sorted(courses_enrolled))}"
        )

    return (
        "You need to enroll in more courses! "
        f"You have to gather {credit_needed - credit_gathered} credits more."
    )
