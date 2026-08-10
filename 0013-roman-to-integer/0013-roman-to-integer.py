class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        f=0
        su=0
        while True:
            if f+1< len(s):
                if d[s[f+1]]> d[s[f]]:
                    su+=(d[s[f+1]]-d[s[f]])
                    f+=2
                else:
                    su+=d[s[f]]
                    f+=1
            else:
                break
        if f != len(s):
            su+=d[s[f]]

        return su
            

        