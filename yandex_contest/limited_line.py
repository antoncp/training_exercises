class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        return self.queue[self.head]

    def get_size(self):
        return self.size


n = int(input())
s = int(input())
a = Queue(s)
com_panel = {
    'push': a.push,
    'pop': a.pop,
    'peek': a.peek,
    'size': a.get_size,
}
for i in range(n):
    action = input().split()
    if action[0] == 'push':
        com_panel[action[0]](int(action[1]))
    else:
        print(com_panel[action[0]]())
