from typing import List


class Book:
    def __init__(self, title: str, author: str, genre: str) -> None:
        self.title = title
        self.author = author
        self.genre = genre
        self.page: int = 0

    def turn_page(self, page: int) -> None:
        self.page = page

    def __str__(self) -> str:
        return f"{self.genre}: {self.title} - {self.author}"

    def __lt__(self, other: "Book") -> bool:
        if self.genre != other.genre:
            return self.genre < other.genre

        if self.title != other.title:
            return self.title < other.title

        return self.author < other.author


class Library:
    def __init__(self, name: str, *books: Book) -> None:
        self.name = name
        self.books: List[Book] = [*books]

    def find_book(self, title: str) -> Book:
        for book in self.books:
            if book.title == title:
                break

        else:
            raise LookupError(f'No such book with title "{title}"')

        return book

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        book = self.find_book(title)

        self.books.remove(book)

    @property
    def books_info(self) -> str:
        return "\n".join(map(str, self.books))

    def sort(self) -> None:
        self.books.sort()
