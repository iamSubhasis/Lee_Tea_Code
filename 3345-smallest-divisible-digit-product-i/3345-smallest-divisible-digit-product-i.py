class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            s=1
            k=str(i)
            for j in k:
                j=int(j)
                s*=j
            if s%t == 0:
                return int(k)


        