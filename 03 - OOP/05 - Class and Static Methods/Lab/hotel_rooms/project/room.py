from typing import Optional


class Room:
    def __init__(self, number: int, capacity: int) -> None:
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int) -> Optional[str]:
        if self.is_taken or self.capacity < people:
            return f"Room number {self.number} cannot be taken"

        self.guests += people
        self.is_taken = True

        return None

    def free_room(self) -> Optional[str]:
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.guests = 0
        self.is_taken = False

        return None
