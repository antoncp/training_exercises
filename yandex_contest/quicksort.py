# Задача "Эффективная быстрая сортировка". ID решения в Я.Контесте 88616542

from dataclasses import dataclass
from typing import List


@dataclass
class User:
    """Represents users for comparison, their names, finished tasks and
    accumulated fines.
    """
    name: str
    tasks: int 
    fine: int

    @classmethod
    def from_text(cls, text: str):
        name, tasks, fine = text.split()
        return cls(name=name, tasks=int(tasks), fine=int(fine))

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return (-self.tasks, self.fine, self.name) < (
            -other.tasks,
            other.fine,
            other.name,
        )


def partition(array: List[User], left: int, right: int) -> int:
    """Compares elements of the array with pivot element, arranges elements
    based on their relation to the pivot element.
    """
    pivot = array[right]
    divider = left - 1
    for element in range(left, right):
        if array[element] < pivot:
            divider += 1
            array[divider], array[element] = array[element], array[divider]
    array[divider + 1], array[right] = array[right], array[divider + 1]
    return divider + 1


def quicksort(array: List[User], left: int, right: int) -> List[User]:
    """Sorts array of users with quicksort algorithm."""
    if left < right:
        pivot = partition(array, left, right)
        quicksort(array, left, pivot - 1)
        quicksort(array, pivot + 1, right)
    return array


if __name__ == "__main__":
    num: int = int(input())
    users: List[User] = [User.from_text(input()) for _ in range(num)]
    sorted_users: List[User] = quicksort(users, left=0, right=num-1)
    print(*sorted_users, sep='\n')
