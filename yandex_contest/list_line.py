class Queue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def put(self, x):
        self.queue.append(x)
        self.size += 1

    def get(self):
        if self.is_empty():
            print('error')
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1)
            self.size -= 1
            print(x)

    def get_size(self):
        print(self.size)


n = int(input())
a = Queue()
com_panel = {
    'put': a.put,
    'get': a.get,
    'size': a.get_size,
}
for i in range(n):
    action = input().split()
    if action[0] == 'put':
        com_panel[action[0]](int(action[1]))
    else:
        com_panel[action[0]]()
