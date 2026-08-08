class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        
        s_to_t = {}
        used = set()

        for i in range(len(s)):
            if s[i] in s_to_t:
                if s_to_t[s[i]]!=t[i]:
                    return False
            
            else:
                if t[i] in used:
                    return False

            s_to_t[s[i]] = t[i]
            used.add(t[i])
        return True