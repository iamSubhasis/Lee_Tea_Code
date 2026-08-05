class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        pres=[0]*(max(nums)+1)
        res=[]
        for i in nums:
             pres[i] =1
        
        for i in range(min(nums),len(pres)):
            if pres[i]==0:
                res.append(i)
        return res