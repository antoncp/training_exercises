a, b = list(reversed([i for i in input()])), [i for i in input()]
for i in b:
    if a and i == a[-1]:
        a.pop()
print(not a)
