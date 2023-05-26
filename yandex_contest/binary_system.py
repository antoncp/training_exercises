a, b = input(), input()
align = max(len(a), len(b))
a = list(map(int, a.rjust(align, '0')))
b = list(map(int, b.rjust(align, '0')))
all = zip(a[::-1], b[::-1])
float = 0
result = ''
for x, y in all:
    res = x + y + float
    if res <= 1:
        result += str(res)
        float = 0
    elif res == 2:
        result += '0'
        float = 1
    elif res == 3:
        result += '1'
        float = 1
if float:
    result += '1'
print(result[::-1])
