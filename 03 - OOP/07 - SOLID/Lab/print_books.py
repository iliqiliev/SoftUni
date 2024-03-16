from abc import ABC, abstractmethod
from collections import deque


class Book:
    def __init__(self, name: str, author: str, content: str) -> None:
        self.name = name
        self.author = author
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def formatting(self, book: Book) -> Book: ...

    def format_book(self, book: Book) -> str:
        return self.formatting(book).content


class Printer:
    def __init__(self, *book_queue: Book) -> None:
        self.book_queue = deque(*book_queue)

    def print_book(self, formatter: Formatter) -> str:
        if not self.book_queue:
            raise IndexError("No books in the print queue.")

        current_book = self.book_queue.popleft()

        return formatter.format_book(current_book)
