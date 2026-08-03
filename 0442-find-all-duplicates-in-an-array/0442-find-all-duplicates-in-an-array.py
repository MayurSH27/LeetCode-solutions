class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        op = []

        for i in nums:
            if i in s:
                op.append(i)
            s.add(i)
        return op