class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        longest, current = 0, 0
        up, down = False, False
        for i in range(1, len(arr)):
            if not current:
                if arr[i] > arr[i - 1]:
                    current += 2
                    up = True
            elif up:
                if arr[i] > arr[i - 1]:
                    current += 1
                elif arr[i] < arr[i - 1]:
                    current += 1
                    up = False
                    down = True
                else:
                    up, down = False, False
                    current = 0
            elif down:
                if arr[i] < arr[i - 1]:
                    current += 1
                elif arr[i] > arr[i - 1]:
                    up, down = True, False
                    longest = max(longest, current)
                    current = 2
                else:
                    up, down = False, False
                    longest = max(longest, current)
                    current = 0
        return longest if up else max(longest, current)
