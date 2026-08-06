class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i,x in enumerate(nums):
            if target-x in h:
                return [h[target-x], i]
            h[x]=i