class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        max_idx = nums.index(max(nums))
        min_idx = nums.index(min(nums))

        left = max(max_idx, min_idx) + 1
        right = n - min(max_idx, min_idx)

        mixed = min(max_idx, min_idx) + 1 + n - max(max_idx, min_idx)

        return min(left, right, mixed)