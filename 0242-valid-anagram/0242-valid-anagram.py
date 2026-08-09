class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}

        for i in s:
            if i in hm1:
                hm1[i] = hm1[i]+1
            else:
                hm1[i]=1
        
        for i in t:
            if i in hm2:
                hm2[i] = hm2[i]+1
            else:
                hm2[i]=1

        if(len(hm1)!=len(hm2)):
            return False

        for i in hm1:
            if i not in hm2:
                return False
            elif hm1[i]!=hm2[i]:
                return False
        return True