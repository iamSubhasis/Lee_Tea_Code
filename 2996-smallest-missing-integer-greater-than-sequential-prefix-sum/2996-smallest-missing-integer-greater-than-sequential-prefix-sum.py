class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        f = 0
        t = 0

        while f < len(nums):
            t += nums[f]

            if f + 1 < len(nums) and nums[f + 1] != nums[f] + 1:
                break

            f += 1

        while t in nums:
            t += 1

        return t