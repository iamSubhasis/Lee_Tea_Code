class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l = []
        d={}
        for i in arr:
            l.append(i)
        l.sort()
        
        counter=1

        for i in l :
            if d != {} :
                if i not  in d:
                    counter +=1
                    d[i]= counter
            else:
                d[i]= counter
        
        for i,v in enumerate(arr):
            arr[i] = d[v]
        return arr
                    





        