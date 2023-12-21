class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        rating = []
        for i in set(nums):
            rating.append((i, nums.count(i)))
        return [i[0] for i in sorted(rating, reverse=True, key=lambda i: i[1])[:k]]
