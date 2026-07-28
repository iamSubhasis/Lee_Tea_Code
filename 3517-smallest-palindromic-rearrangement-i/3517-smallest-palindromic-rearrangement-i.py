class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # if len(s) == 1:
        #     return s
        # z=[]
        # for i in s:
        #     z.append(i)
        # z.sort()
        # n_s=""
        # res=[]
        # i=0
        # j=1

        # while i<len(z) and j< len(z):
        #     if z[i] == z[j]:
        #         res.append(z[i])
        #         i+=2
        #         j+=2
        #     elif z[i]!= z[j]:
        #         i+=2
        #         n_s=z[i]
        # if len(z) %2!=0:
        #     if n_s !="" :
        #         res.append(n_s)
        #     else:
        #         res.append(z[-1])
        #     res = res+ res[-2::-1]
        # else:
        #     res=res+res[-1::-1]

        # return "".join(res)
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

        



        
        