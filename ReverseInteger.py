class Solution:
    def reverse(self, x: int) -> int:
        minus = True if str(x).startswith('-') else False
        answer = int(str(x)[::-1].strip('-')) 
        if answer > 2**31:
            return 0
        return -answer if minus else answer
