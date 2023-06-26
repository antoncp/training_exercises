# Задача "Поиск в сломанном массиве". ID решения в Я.Контесте 88564639

import sys
from typing import List, Optional

sys.setrecursionlimit(3000)


def broken_search(
    nums: List[str], target: int, left: int = 0, right: Optional[int] = None
) -> int:
    """Conducts binary search in a shifted array with recursion workflow."""
    if not right:
        right = len(nums) - 1
    if right < left:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[left] <= nums[mid]:
        return (
            broken_search(nums, target, left, mid)
            if nums[left] <= target < nums[mid]
            else broken_search(nums, target, mid + 1, right)
        )
    else:
        return (
            broken_search(nums, target, mid + 1, right)
            if nums[mid] < target <= nums[right]
            else broken_search(nums, target, left, mid)
        )


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
