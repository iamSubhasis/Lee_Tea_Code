class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.check(s) == self.check(t)

    def check(self,l: list):
        st=[]
        for i in list(l):
            if i == "#":
                if len(st) > 0:
                    st.pop()
            else:
                st.append(i)
        return "".join(st)