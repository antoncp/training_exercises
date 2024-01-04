import re


def isSubsequence(s: str, t: str) -> bool:
    mask = ".*".join(s)
    x = re.search(mask, t)
    return True if x else False


# or


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cursor = 0
        for i in t:
            if cursor < len(s) and i == s[cursor]:
                cursor += 1
        return True if cursor == len(s) else False
