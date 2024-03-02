from typing import Union
from project import User, Library


class Registration:
    def add_user(self, user: User, library: Library) -> Union[str, None]:
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

        return None

    def remove_user(self, user: User, library: Library) -> Union[str, None]:
        if user not in library.user_records:
            return "We could not find such user to remove!"

        library.user_records.remove(user)

        return None

    def change_username(
        self, user_id: int, new_name: str, library: Library
    ) -> str:

        for user in library.user_records:
            if user.user_id == user_id:
                if user.username == new_name:
                    return (
                        "Please check again the provided username - "
                        "it should be different than the username used so far!"
                    )

                break
        else:
            return f"There is no user with id = {user_id}!"

        if user.username in library.rented_books:
            library.rented_books[new_name] = library.rented_books.pop(user.username)

        user.username = new_name

        return f"Username successfully changed to: {new_name} for user id: {user_id}"
