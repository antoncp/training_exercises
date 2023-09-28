from functools import lru_cache


class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n in (0, 1):
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
