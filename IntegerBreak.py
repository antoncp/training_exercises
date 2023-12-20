class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        full3 = n // 3
        rest3 = n % 3
        if n <= 3:
            return n - 1
        if rest3:
            if rest3 == 1:
                return (3 ** (full3 - 1)) * 4
            if rest3 == 2:
                return (3 ** full3) * 2
        return 3 ** full3
