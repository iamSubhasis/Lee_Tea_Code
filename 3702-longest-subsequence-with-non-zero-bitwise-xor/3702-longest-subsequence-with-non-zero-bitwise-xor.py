class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        totl =  notzero =0

        for n in nums:
            notzero |= n >0
            totl ^= n
        return notzero*(len(nums)- (not totl))
        