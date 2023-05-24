# Задача "Ловкость рук". ID решения в Я.Контесте 87636017

from collections import Counter

k = int(input())
keyboard = []
for i in range(4):
    keyboard.extend(i for i in list(input()) if i.isdigit())

result = 0
for i in Counter(keyboard).values():
    if k*2 >= i:
        result += 1

print(result)
