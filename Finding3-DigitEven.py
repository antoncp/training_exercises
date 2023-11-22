from itertools import permutations


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        vars = [
            int(f"{x[0]}{x[1]}{x[2]}")
            for x in permutations(digits, 3)
            if x[0] != 0
        ]
        return sorted([i for i in set(vars) if i % 2 == 0])
