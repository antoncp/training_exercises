class Solution:
    def mySqrt(self, x: int) -> int:
        y, d = 0, 0
        while y < x:
            d += 1
            y = d*d
        return d if y == x else d-1
