class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            print('error')

    def get_max(self):
        try:
            print(max(self.items))
        except ValueError:
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
