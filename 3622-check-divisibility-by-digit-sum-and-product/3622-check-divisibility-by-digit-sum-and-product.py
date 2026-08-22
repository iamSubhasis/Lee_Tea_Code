class Solution:
    def checkDivisibility(self, n: int) -> bool:
        l=list(map(int,str(n)))
        k=1
        for i in l:
            k *= i
        return n%(sum(l)+k)==0