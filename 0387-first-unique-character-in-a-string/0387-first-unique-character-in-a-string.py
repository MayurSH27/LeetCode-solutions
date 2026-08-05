class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s)

        for i,c in enumerate(s):
            if freq[s[i]]==1:
                return i
        return -1