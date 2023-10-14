class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        for x, i in enumerate(nums):
            if i == nums[x-1]:
                nums[x-1] = 101
        while 101 in nums:
            nums.remove(101)
        return len(nums)
    