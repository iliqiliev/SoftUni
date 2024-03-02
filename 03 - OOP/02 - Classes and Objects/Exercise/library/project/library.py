from collections import defaultdict
from typing import Dict, List, Union
from project import User


class Library:
    def __init__(self) -> None:
        self.user_records: List[User] = []
        self.books_available: Dict[str, List[str]] = {}
        self.rented_books: Dict[str, Dict[str, int]] = defaultdict(dict)

    def get_book(
        self, author: str, book_name: str, days_to_return: int, user: User
    ) -> str:

        for books_info in self.rented_books.values():
            if book_name in books_info:
                return (
                    f'The book "{book_name}" is already rented and '
                    f'will be available in {books_info[book_name]} days!'
                )

        # it is assumed that the book is available
        user.books.append(book_name)
        self.books_available[author].remove(book_name)
        self.rented_books[user.username][book_name] = days_to_return

        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(
        self, author: str, book_name: str, user: User
    ) -> Union[str, None]:

        username = user.username

        if book_name not in self.rented_books[username]:
            return f"{username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        self.rented_books[username].pop(book_name)

        return None
