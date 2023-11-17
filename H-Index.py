class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for num, i in enumerate(citations):
            if num > i:
                return prev if (prev := citations[num - 1]) <= num - 1 else num
        return (
            len(citations) if citations[-1] > len(citations) else citations[-1]
        )
