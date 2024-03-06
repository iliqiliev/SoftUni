from typing import Union


class Account:
    def __init__(self, _id: int, balance: float, pin: int) -> None:
        self.__id = _id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin: int) -> Union[int, str]:
        if self.__pin != pin:
            return "Wrong pin"

        return self.__id

    def change_pin(self, old: int, new: int) -> str:
        if self.__pin != old:
            return "Wrong pin"

        self.__pin = new

        return "Pin changed"
