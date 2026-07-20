class Solution:
    def binaryGap(self, n: int) -> int:
        if n.bit_count() == 1:
            return 0
        else:
            res=0
            l1=0
            s=bin(n)
            s=s[2:]
            for i in range(1,len(s)):
                if s[i] == "1":
                    if i -l1 > res: 
                        res = i- l1
                    l1=i
            return res



        