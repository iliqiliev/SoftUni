class Book:  # pylint: disable=too-few-public-methods
    def __init__(self, name: str, author: str, pages: int) -> None:
        self.name = name
        self.author = author
        self.pages = pages
