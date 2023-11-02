class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_s = [i for i in s.lower() if i.isalnum()]
        return clear_s == clear_s[::-1]
