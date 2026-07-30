class Solution:
    def minimumPushes(self, word: str) -> int:
        c=0
        l=len(word)
        res=0
        while l > 0:
            c+=1
            
            if l > 8 :
                res += 8*c
            else:
                res += l*c
            l-=8
        return res


        