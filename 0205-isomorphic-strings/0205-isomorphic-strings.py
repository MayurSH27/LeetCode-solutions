class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False

        hm = {}

        for i in range(len(s)):
            if s[i] in hm and hm[s[i]]!=t[i]:
                return False
            elif s[i] not in hm and t[i] in hm.values():
                return False
            else:
                hm[s[i]] = t[i]
        return True