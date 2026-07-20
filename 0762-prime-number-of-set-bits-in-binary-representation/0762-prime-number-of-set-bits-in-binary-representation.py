class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res=0
        prime=[2,3,5,7,11,13,17,19]
        prime=set(prime)


        for i in range(left,right+1):
            s=bin(i)
            count=0
            for i in s:
                if i=="1":
                    count+=1
            if count in prime:
                res+=1

        return res
        