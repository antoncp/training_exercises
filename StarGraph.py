from collections import Counter

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        plain = [i for j in edges[:5] for i in j]
        return Counter(plain).most_common(1)[0][0]
