class Solution:
    def minimumPushes(self, word: str) -> int:
        ch=[0]*26
        push=1
        res=0
        count=1
        for i in word :
            ch[ord(i)-97] +=1
        ch.sort(reverse=True)
        for i in range(26):
            if ch[i] == 0:
                break
            if count > 8:
                count=0
                push+=1
            res +=(ch[i]*push)
            count+=1
        return res


        


        