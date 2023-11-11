class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        reverse_vowels = [v for v in s if v in vowels]
        new_s = [i if i not in vowels else reverse_vowels.pop() for i in s]
        return "".join(new_s)
