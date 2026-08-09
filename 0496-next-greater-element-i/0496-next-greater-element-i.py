class Solution:
    def nextGreaterElement(self, q: List[int], a: List[int]) -> List[int]:
        n=len(a)
        ans = {}
        st=[]
        for i in range(n-1,-1,-1):
            while len(st) != 0 and st[-1] <= a[i]:
                st.pop()
            if len(st) == 0:
                ans[a[i]]= -1
            else:
                ans[a[i]]= st[-1]
            st.append(a[i])
        st=[]

        for i in q:
            st.append(ans[i])
        return st

                
        