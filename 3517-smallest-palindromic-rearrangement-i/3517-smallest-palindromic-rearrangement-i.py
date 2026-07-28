class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        d={}
        z=[]
        for i in s:
            z.append(i)
        z.sort()
        for i in z:
            d[i]= d.get(i,0)+1
        res=[]
        for i in d:
            if d[i] %2 == 0:
                v=i*(d[i]//2)
                res.append(v)
            else :
                v=i*(d[i]//2)
                d[i]=1
                res.append(v)
        for i in d:
            if d[i] == 1:
                res.append(i)
        if len(s)%2 != 0:
            res = res + res[-2::-1]
        else:
            res = res + res[-1::-1]
        return "".join(res)

        



        
        