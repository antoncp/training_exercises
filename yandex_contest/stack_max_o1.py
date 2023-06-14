class StackMax:
    def __init__(self):
        self.items = []
        self.max = None

    def push(self, item):
        self.items.append(item)
        if not self.max:
            self.max = item
        elif self.max <= item:
            self.max = item

    def pop(self):
        try:
            last = self.items.pop()
        except IndexError:
            print('error')
        else:
            if last == self.max and self.items:
                self.max = max(self.items)
            elif last == self.max:
                self.max = None

    def get_max(self):
        if self.max:
            print(self.max)
        else:
            print('None')


a = StackMax()
com_panel = {
    'push': a.push,
    'pop': a.pop,
    'get_max': a.get_max,
}
n = int(input())
for i in range(n):
    action = input().split()
    if action[0] == 'push':
        com_panel[action[0]](int(action[1]))
    else:
        com_panel[action[0]]()
