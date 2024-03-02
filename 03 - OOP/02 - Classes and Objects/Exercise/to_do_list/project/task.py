from typing import List


class Task:
    def __init__(self, name: str, due_date: str) -> None:
        self.name = name
        self.due_date = due_date
        self.comments: List[str] = []
        self.completed = False

    def change_name(self, new_name: str) -> str:
        if self.name == new_name:
            return "Name cannot be the same."

        self.name = new_name

        return self.name

    def change_due_date(self, new_date: str) -> str:
        if self.due_date == new_date:
            return "Date cannot be the same."

        self.due_date = new_date

        return self.due_date

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, index: int, new_comment: str) -> str:
        if not 0 <= index < len(self.comments):
            return "Cannot find comment."

        self.comments[index] = new_comment

        return ", ".join(self.comments)

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"
