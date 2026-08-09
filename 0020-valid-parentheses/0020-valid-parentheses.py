class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0 :
            return False
        st=[]
        for ch in list(s):
            if ch in "({[":
                st.append(ch)
            elif ch in ")}]":
                if len(st) == 0:
                    return False
                x=st.pop()
                if ch == ")" and x != "(":
                    return False
                elif ch == "]" and x != "[":
                    return False
                elif ch == "}" and x != "{":
                    return False
        if len(st) != 0:
            return False
        return True