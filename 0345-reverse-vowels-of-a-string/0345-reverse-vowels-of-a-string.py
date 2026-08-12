class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        stolist = list(s)

        l = 0
        r = len(s)-1

        while l<r:
            while l<r and stolist[l] not in vowels:
                l+=1
            while l<r and stolist[r] not in vowels:
                r-=1
            if l<r:
                stolist[l], stolist[r] = stolist[r], stolist[l]
                l+=1
                r-=1
        return "".join(stolist)