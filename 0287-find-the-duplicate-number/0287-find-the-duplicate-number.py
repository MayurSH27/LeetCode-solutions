class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm = {}
        for i in nums:
            if i in hm:
                return i
            else:
                hm[i]=1
                