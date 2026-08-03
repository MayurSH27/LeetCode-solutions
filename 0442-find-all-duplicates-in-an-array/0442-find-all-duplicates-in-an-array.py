class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hm = {}
        op = []

        for i in nums:
            if i in hm:
                hm[i]+=1
                op.append(i)
            hm[i]=1

        return op