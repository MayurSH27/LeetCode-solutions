class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        psum = 0
        submax = nums[0]

        for i in nums:
            psum = max(psum+i, i)
            submax = max(submax, psum)
        return submax