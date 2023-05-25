# Задача "Ловкость рук". ID решения в Я.Контесте 87652101

from collections import Counter
from typing import List


def count_points(k: int, keyboard: List[int]) -> int:
    """Counts the number of possible points in the game."""
    result = 0
    for i in Counter(keyboard).values():
        if k*2 >= i:
            result += 1
    return result


if __name__ == '__main__':
    k = int(input())
    keyboard = [i for _ in range(4) for i in list(input()) if i.isdigit()]
    print(count_points(k, keyboard))
