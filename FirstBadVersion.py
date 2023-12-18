class Solution(object):
    def firstBadVersion(self, n, left=0, right=None):
        """
        :type n: int
        :rtype: int
        """
        if not right:
            right = n
        mid = (left + right) // 2
        if right <= left:
            return mid
        if isBadVersion(mid):
            return self.firstBadVersion(n, left, mid)
        else:
            return self.firstBadVersion(n, mid + 1, right)
