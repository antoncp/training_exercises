class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        for i in set(nums):
            if nums.count(i) > size/2:
                return i
