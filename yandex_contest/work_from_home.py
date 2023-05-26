x = int(input())
result = ""
while x != 0:
    result += str((x % 2))
    x = x // 2
print(result[::-1] if result else '0')
