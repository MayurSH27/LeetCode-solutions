class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        s1 = list(s)
        t1 = list(t)

        s1.sort()
        t1.sort()

        for i in range(len(s)):
            if(s1[i]!=t1[i]):
                return False
        return True