class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        all = 0
        for i in set(nums):
            n = nums.count(i)
            all += n * (n - 1) // 2
        return all
