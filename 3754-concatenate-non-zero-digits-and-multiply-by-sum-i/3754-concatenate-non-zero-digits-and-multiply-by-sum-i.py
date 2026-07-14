class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n= str(n)
        res=""
        sum=0
        if n == "0":
            return 0
        else:
            for i in n:
                if i != "0":
                    res+=i
                    sum+=int(i)

        return int(res)*sum
    
