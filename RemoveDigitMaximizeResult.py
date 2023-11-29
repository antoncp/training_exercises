class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        x = -1
        all = []
        while True:
            x = number.find(digit, x+1)
            if x == -1:
                break
            all.append(int(number[:x] + number[x + 1:]))
        return str(max(all))

