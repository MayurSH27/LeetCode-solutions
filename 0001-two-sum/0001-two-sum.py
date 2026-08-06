class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        i = 0
        ans = []

        for x in nums:
            if (target-x in hm.keys()):
                ans.append(i)
                ans.append(hm.get(target-x))
            else:
                hm[x]=i
            i+=1
        return ans