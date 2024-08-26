class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        indices = []
        index = -1 
        while True:
            index = number.find(digit, index + 1)
            if index == -1:
                break
            indices.append(index)
        options = [int(number[:i] + number[i+1:]) for i in indices]
        return str(max(options))
