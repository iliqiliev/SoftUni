from math import ceil
from typing import List


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, count: int) -> "PhotoAlbum":
        return cls(ceil(count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str) -> str:
        for page_index, page in enumerate(self.photos):
            slot_index = len(page)

            if slot_index < self.PHOTOS_PER_PAGE:
                self.photos[page_index].append(label)

                return (
                    f"{label} photo added successfully on "
                    f"page {page_index + 1} slot {slot_index + 1}"
                )

        return "No more free slots"

    def display(self) -> str:
        separator = "-" * 11
        photo_representation = "[] "

        result = [separator]

        for page in range(self.pages):
            result.extend([
                (photo_representation * len(self.photos[page])).rstrip(),
                separator
            ])

        return "\n".join(result)
