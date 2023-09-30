class Solution:
    def findDifference(self, nums1, nums2):
        return [
            list(set(nums1).difference(set(nums2))),
            list(set(nums2).difference(set(nums1))),
        ]
