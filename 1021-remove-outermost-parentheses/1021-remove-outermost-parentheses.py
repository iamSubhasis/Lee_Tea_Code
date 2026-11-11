class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        res=[]
        for i in s :
            if i == "(":
                c+=1
            elif i == ")":
                c-=1
            if c != 0 and i == ")":
                res.append(i)
            if c != 1 and i == "(":
                res.append(i)
        return "".join(res)
            
            
        