class Solution:
    def minimumPushes(self, word: str) -> int:
        ch = [0] * 26
        
        for c in word:
            ch[ord(c) - ord('a')] += 1
        
        ch.sort(reverse=True)

        res = 0
        for i in range(26):
            if ch[i] == 0:
                break
            
            push = (i // 8) + 1
            res += ch[i] * push
        
        return res


        


        