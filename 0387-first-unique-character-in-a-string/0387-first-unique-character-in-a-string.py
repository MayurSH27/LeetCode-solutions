class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}

        for char in s:
            if char in hm:
                hm[char] = hm[char]+1
            else:
                hm[char]=1
        for i,c in enumerate(s):
            if hm[c]==1:
                return i
        return -1