from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Iliya")

    def test_init(self) -> None:
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Iliya", self.student.name)

        self.assertEqual({1: 2}, Student("", {1: 2}).courses)

    def test_enroll_add_notes(self) -> None:
        course_name = "test"
        notes = [1, 2, 3]

        result = self.student.enroll(course_name, notes)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(notes, self.student.courses[course_name])

    def test_enroll_add_notes_explicitly(self) -> None:
        course_name = "test"
        notes = [1, 2, 3]

        result = self.student.enroll(course_name, notes, "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(notes, self.student.courses[course_name])

    def test_enroll_already_added(self) -> None:
        course_name = "test"
        notes = [1, 2, 3]

        self.student.enroll(course_name, notes.copy())
        result = self.student.enroll(course_name, notes.copy())
        self.assertEqual(
            "Course already added. Notes have been updated.", result
        )
        self.assertEqual(notes * 2, self.student.courses[course_name])

    def test_enroll_course_only(self) -> None:
        course_name = "test"

        result = self.student.enroll(course_name, None, "N")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses[course_name])

    def test_add_notes_successfully(self) -> None:
        course_name = "test"

        self.student.enroll(course_name, None, "N")

        result = self.student.add_notes(course_name, 1)
        self.assertEqual("Notes have been updated", result)
        self.assertEqual([1], self.student.courses[course_name])

    def test_add_notes_no_such_course(self) -> None:
        with self.assertRaises(Exception) as error:
            self.student.add_notes("test", 1)

        self.assertEqual(
            "Cannot add notes. Course not found.", str(error.exception)
        )

    def test_leave_course_successfully(self) -> None:
        course_name = "test"

        self.student.enroll(course_name, None, "N")

        result = self.student.leave_course(course_name)
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_leave_course_no_such_course(self) -> None:
        with self.assertRaises(Exception) as error:
            self.student.leave_course("test")

        self.assertEqual(
            "Cannot remove course. Course not found.", str(error.exception)
        )


if __name__ == "__main__":
    main()
