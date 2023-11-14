class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_array = sorted(nums)
        if sorted_array[0] != 0:
            return 0
        for i in range(1, len(sorted_array)):
            if sorted_array[i] - sorted_array[i-1] > 1:
                return sorted_array[i] - 1  
        return sorted_array[-1] + 1
