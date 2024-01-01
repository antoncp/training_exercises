class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        final_order = []
        for word in words:
            letter_sec = []
            for letter in word:
                letter_sec.append(order.index(letter))
            final_order.append((word, letter_sec))
        final_order = [
            word[0] for word in sorted(final_order, key=lambda x: x[1])
        ]
        return words == final_order
