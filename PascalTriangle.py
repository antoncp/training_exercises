from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            line = []
            if i == 0:
                line.append(1)
            else:
                prev = [0] + result[i - 1] + [0]
                for j in range(len(prev)-1):
                    line.append(prev[j] + prev[j+1])
            result.append(line)
        return result
