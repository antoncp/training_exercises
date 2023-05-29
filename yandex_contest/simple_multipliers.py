x = int(input())
y = 2
limit = x ** 0.5
multi = []
while x != 1:
    if x % y == 0:
        x = x / y
        multi.append(int(y))
        y = 2
    else:
        y += 1
        if y > limit:
            y = x
print(*sorted(multi))
