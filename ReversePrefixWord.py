class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        border = word.find(ch)
        if border != -1:
            return word[border::-1] + word[border+1:]
        else:
            return word
