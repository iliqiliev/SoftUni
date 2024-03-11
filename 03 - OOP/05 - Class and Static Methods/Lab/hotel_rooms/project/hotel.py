from typing import List, Optional
from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars: int) -> "Hotel":
        return cls(f"{stars} stars Hotel")

    def _find_room(self, room_number: int) -> Optional[Room]:
        for room in self.rooms:
            if room.number == room_number:
                return room

        return None

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        room = self._find_room(room_number)

        if room is not None:
            room.take_room(people)
            self.guests += room.guests

    def free_room(self, room_number: int):
        room = self._find_room(room_number)

        if room is not None:
            self.guests -= room.guests
            room.free_room()

    def status(self) -> str:
        free, taken = [], []
        for room in self.rooms:
            if room.is_taken:
                taken.append(str(room.number))

            else:
                free.append(str(room.number))

        return (
            f"Hotel {self.name} has {self.guests} total guests\n"
            f"Free rooms: {', '.join(free)}\n"
            f"Taken rooms: {', '.join(taken)}"
        )
