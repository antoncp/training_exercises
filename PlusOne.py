class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_one = int("".join(map(str, digits)))+1
        return map(int, list(str(plus_one)))
