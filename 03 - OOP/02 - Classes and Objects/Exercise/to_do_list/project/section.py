from typing import List
from project import Task


class Section:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        for task in self.tasks:
            if task.name == task_name:
                break

        else:
            return f"Could not find task with the name {task_name}"

        task.completed = True

        return f"Completed task {task_name}"

    def clean_section(self) -> str:
        removed_tasks = 0

        for index, task in enumerate(self.tasks):
            if task.completed:
                self.tasks.pop(index)
                removed_tasks += 1

        return f"Cleared {removed_tasks} tasks."

    def view_section(self) -> str:
        result = [
            f"Section {self.name}:",
            *(task.details() for task in self.tasks)
        ]

        return "\n".join(result)
