class Solution(object):
    def getKth(self, lo, hi, k):
        transform = []
        steps = 0
        for i in range(lo, hi+1):
            initial = i
            while i != 1:
                steps += 1
                if i % 2 == 0:
                    i = i / 2
                else:
                    i = i * 3 + 1
            transform.append((steps, initial))
            steps = 0
        return sorted(transform)[k-1][1]
