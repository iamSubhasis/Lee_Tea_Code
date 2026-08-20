class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        d={}
        for i in nums:
            d[i] = d.get(i,0)+1
        
        t=-1

        if k == 1:
            for i in d :
                if d[i] == 1:
                    t=max(i,t)
            return t
        
        ma,mi=max(nums[0],nums[-1]),min(nums[0],nums[-1])
        if d[ma] == 1:
            return ma
        elif d[mi] == 1:
            return mi
        return -1
        
