# Задача "Дек". ID решения в Я.Контесте 88067668

from typing import List, Union


class Deque:
    """Class, realizing a two-side queue (deque)."""
    def __init__(self, max_limit: int):
        self.__queue: List[Union[int, None]] = [None] * max_limit
        self.max_n: int = max_limit
        self.__head: int = 0
        self.__tail: int = 0
        self.__size: int = 0

    @property
    def is_empty(self) -> bool:
        """Checks is the deque empty or not."""
        return self.__size == 0

    @property
    def is_full(self) -> bool:
        """Checks is the deque full or not."""
        return self.__size == self.max_n

    def push_back(self, new_element: int) -> None:
        """Adds element at the end of the deque."""
        if not self.is_full:
            self.__queue[self.__tail] = new_element
            self.__tail = (self.__tail + 1) % self.max_n
            self.__size += 1
        else:
            raise IndexError('The deque is already full')

    def push_front(self, new_element: int) -> None:
        """Adds element at the start of the deque."""
        if not self.is_full:
            self.__head = (self.__head - 1) % self.max_n
            self.__queue[self.__head] = new_element
            self.__size += 1
        else:
            raise IndexError('The deque is already full')

    def pop_back(self) -> str:
        """Removes element from the end of the deque and return it."""
        if self.is_empty:
            raise IndexError('The deque is empty')
        self.__tail = (self.__tail - 1) % self.max_n
        last_element = self.__queue[self.__tail]
        self.__queue[self.__tail] = None
        self.__size -= 1
        return str(last_element)

    def pop_front(self) -> str:
        """Removes element from the start of the deque and return it."""
        if self.is_empty:
            raise IndexError('The deque is empty')
        first_element = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.max_n
        self.__size -= 1
        return str(first_element)


if __name__ == '__main__':
    num_commands: int = int(input())
    max_limit: int = int(input())
    queue: Deque = Deque(max_limit)
    command_panel = {
        'push_back': queue.push_back,
        'push_front': queue.push_front,
        'pop_front': queue.pop_front,
        'pop_back': queue.pop_back,
    }
    COMMAND, ARGUMENT = 0, 1
    for _ in range(num_commands):
        action = input().split()
        if action[COMMAND] == 'push_back' or action[COMMAND] == 'push_front':
            try:
                command_panel[action[COMMAND]](int(action[ARGUMENT]))
            except IndexError:
                print('error')
        else:
            try:
                print(command_panel[action[COMMAND]]())
            except IndexError:
                print('error')
