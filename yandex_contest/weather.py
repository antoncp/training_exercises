period = input()
temp = [-274] + list(map(int, input().split())) + [-274]
days = 0
for i in range(1, len(temp)):
    if temp[i-1] < temp[i] > temp[i+1]:
        days += 1
print(days)
