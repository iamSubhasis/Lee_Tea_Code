class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            l=[0]*26
            for j in i:
                val=ord(j)%97
                l[val]=l[val]+1
            l=tuple(l)
            if l in d:
                d[l].append(i)
            else:
                d[l]=[]
                d[l].append(i)
        res=[]
        for i in d:
            res.append(d[i])
        return res


        
        