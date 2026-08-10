class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 2):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since array is sorted, this is impossible
            if nums[i] > 0:
                break

            j = i + 1
            k = n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicate j values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate k values
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif s < 0:
                    j += 1

                else:
                    k -= 1

        return ans