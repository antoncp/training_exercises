# Задача "Калькулятор". ID решения в Я.Контесте 88061792

from typing import List

OPERATORS = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x // y}


class Stack:
    """Class, realizing a basic stack."""
    def __init__(self):
        self.__queue: List[int] = []

    def put(self, x: int) -> None:
        """Adds element at the top of the stack."""
        self.__queue.append(x)

    def get(self) -> int:
        """Removes element from the top of the stack and return it."""
        if not self.__queue:
            return None
        else:
            return self.__queue.pop()


def calculate_the_list(entry_list: List[str]) -> int:
    """Handles all mathematical operations inside the list with polish
    notation.
    """
    processing_list = Stack()
    for element in entry_list:
        if element in OPERATORS:
            operand_2 = processing_list.get()
            operand_1 = processing_list.get()
            result = OPERATORS[element](operand_1, operand_2)
            processing_list.put(result)
        else:
            processing_list.put(int(element))
    return processing_list.get()


if __name__ == '__main__':
    print(calculate_the_list(input().split()))
