import unittest
from typing import Union


class Integer:
    ROMAN_NUMERALS = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, value: float) -> Union["Integer", str]:
        if not isinstance(value, float):
            return "value is not a float"

        return cls(int(value))

    @classmethod
    def from_roman(cls, roman: str) -> "Integer":
        int_value = cls.ROMAN_NUMERALS[roman[0]]

        for index in range(1, len(roman)):
            last = cls.ROMAN_NUMERALS[roman[index - 1]]
            current = cls.ROMAN_NUMERALS[roman[index]]

            if last < current:
                int_value += current - 2 * last
                continue

            int_value += current

        return cls(int_value)

    @classmethod
    def from_string(cls, value: str) -> Union["Integer", str]:
        if not isinstance(value, str):
            return "wrong type"

        return cls(int(value))
