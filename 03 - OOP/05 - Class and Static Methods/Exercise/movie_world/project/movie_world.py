from itertools import chain
from typing import List, TypeVar
from project import DVD, Customer


Item = TypeVar("Item", DVD, Customer)


class MovieWorld:
    _DVD_CAPACITY = 15
    _CUSTOMER_CAPACITY = 10

    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @classmethod
    def dvd_capacity(cls) -> int:
        return cls._DVD_CAPACITY

    @classmethod
    def customer_capacity(cls) -> int:
        return cls._CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def __get_item(self, item_id: int, items: List[Item]) -> Item:
        try:
            return next(item for item in items if item.id == item_id)

        except StopIteration as error:
            raise LookupError from error

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        try:
            customer = self.__get_item(customer_id, self.customers)
            dvd = self.__get_item(dvd_id, self.dvds)

        except LookupError:
            return "Invalid ID provided"

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return (
                f"{customer.name} should be at least "
                f"{dvd.age_restriction} to rent this movie"
            )

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)

        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id) -> str:
        try:
            customer = self.__get_item(customer_id, self.customers)
            dvd = self.__get_item(dvd_id, self.dvds)

        except LookupError:
            return "Invalid ID provided"

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)

        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self) -> str:
        customers = (str(customer) for customer in self.customers)
        dvds = (str(dvd) for dvd in self.dvds)

        return "\n".join(chain(customers, dvds))
