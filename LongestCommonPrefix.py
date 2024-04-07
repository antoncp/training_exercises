class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sample = strs[0]
        for word in strs[1:]:
            if not sample:
                return ""
            for i in range(min(len(word), len(sample))):
                if word[i] != sample[i]:
                    sample = sample[:i]
                    break
            sample = sample[:min(len(word), len(sample))]
        return sample
