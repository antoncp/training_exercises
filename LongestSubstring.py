class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        already = []
        max_val = 1
        cur = 0
        for i in s:
            if i in already:
                max_val = max(max_val, cur)
                while already:
                    res = already.pop(0)
                    if res == i:
                        already.append(i)
                        cur = len(already)
                        break
            else:
                cur += 1
                already.append(i)
        return max(max_val, cur)
