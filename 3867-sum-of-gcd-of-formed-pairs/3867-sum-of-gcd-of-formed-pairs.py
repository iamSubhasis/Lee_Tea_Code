class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        tema=nums[0]
        pre=[]
        for i in nums:
            if tema < i :
                tema = i
            pre.append(gcd(tema,i))
        pre.sort()
        i=0
        j=len(pre)-1
        gpre=[]
        su=0
        for k in range(len(nums)//2):
            su+=gcd(pre[i],pre[j])
            i+=1
            j-=1
        return su


        