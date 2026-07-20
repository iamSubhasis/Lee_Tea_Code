class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        temp_l=[]
        res=[0]*(len(grid)*len(grid[0]))
        for i in grid:
            for j in i:
                temp_l.append(j)
        for i,v in enumerate(temp_l):
            res[(i+k)%(len(grid)*len(grid[0]))]+=v
        ind = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = res[ind]
                ind+=1
        return grid

        
        