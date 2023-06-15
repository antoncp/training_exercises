class StackMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if not self.stack:
            return "error"
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        return self.stack.pop()

    def get_max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]


n = int(input())
stack = StackMax()
for _ in range(n):
    command = input().split()

    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        result = stack.pop()
        if result == "error":
            print("error")
    elif command[0] == "get_max":
        max_num = stack.get_max()
        print(max_num)
