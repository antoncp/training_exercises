class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 0
        while n >= 0:
            row += 1
            n -= row
        return row - 1
