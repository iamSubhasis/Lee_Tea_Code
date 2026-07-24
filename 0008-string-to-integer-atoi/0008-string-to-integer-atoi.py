class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        res=0
        sign=1
        if len(s) > 0 :
            if s[0] in "+-" :
                sign=-1 if s[0] == "-" else 1
                s=s[1:]
        else:
            return 0

        for i in s:
            if i.isdigit():
                res=(res*10) + int(i)
            else:
                break
        res = res*sign
        if res > (2**31 -1) or res < -2**31:
            if res > 2**31 -1 :
                return 2**31 -1
            else :
                return -2**31
        else:
            return res
        
        