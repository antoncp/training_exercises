# Задача "Эффективная быстрая сортировка". ID решения в Я.Контесте 88580246

from typing import List, Tuple


def partition(array: Tuple[str, int, int], left: int, right: int) -> int:
    """Compares elements of the array with pivot element, arranges elements
    based on their relation to the pivot element.
    """
    pivot = array[right]
    divider = left - 1
    for element in range(left, right):
        if compare_users(array[element], pivot):
            divider += 1
            array[divider], array[element] = array[element], array[divider]
    array[divider + 1], array[right] = array[right], array[divider + 1]
    return divider + 1


def compare_users(
    user_1: Tuple[str, int, int], user_2: Tuple[str, int, int]
) -> bool:
    """Compares two users by finished tasks, accumulated fines and names."""
    return (-user_1[1], user_1[2], user_1[0]) < (
        -user_2[1],
        user_2[2],
        user_2[0],
    )


def quicksort(
    array: List[List[Tuple[str, int, int]]], left: int, right: int
) -> List[List[Tuple[str, int, int]]]:
    """Sorts array of users with quicksort algorithm."""
    if left < right:
        pivot = partition(array, left, right)
        quicksort(array, left, pivot - 1)
        quicksort(array, pivot + 1, right)
    return array


if __name__ == "__main__":
    num = int(input())
    users = [input().split() for _ in range(num)]
    users = [(name, int(tasks), int(fine)) for name, tasks, fine in users]
    for user in quicksort(users, left=0, right=num - 1):
        print(user[0])
