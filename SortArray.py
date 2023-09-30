class Solution:
    def sortArrayByParity(self, nums):
        even = [i for i in nums if i % 2 == 0]
        odd = [i for i in nums if i % 2 != 0]
        return even + sorted(odd)
