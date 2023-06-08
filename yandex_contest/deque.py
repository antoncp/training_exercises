# Задача "Дек". ID решения в Я.Контесте 88044562

class Queue:
    """Class, realizing a two-side queue (deque)."""
    def __init__(self, max_limit: int):
        self.queue: list = [None] * max_limit
        self.max_n: int = max_limit
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0

    def is_empty(self) -> bool:
        """Checks is the queue empty or not."""
        return self.size == 0

    def push_back(self, x: int) -> None:
        """Adds element at the end of the queue."""
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def push_front(self, x: int) -> None:
        """Adds element at the start of the queue."""
        if self.size != self.max_n:
            self.head = (self.head - 1) % self.max_n
            self.queue[self.head] = x
            self.size += 1
        else:
            print('error')

    def pop_back(self) -> str:
        """Removes element from the end of the queue and return it."""
        if self.is_empty():
            return 'error'
        self.tail = (self.tail - 1) % self.max_n
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        self.size -= 1
        return str(x)

    def pop_front(self) -> str:
        """Removes element from the start of the queue and return it."""
        if self.is_empty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return str(x)


if __name__ == '__main__':
    num_commands: int = int(input())
    max_limit: int = int(input())
    queue: Queue = Queue(max_limit)
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
            command_panel[action[COMMAND]](int(action[ARGUMENT]))
        else:
            print(command_panel[action[COMMAND]]())
