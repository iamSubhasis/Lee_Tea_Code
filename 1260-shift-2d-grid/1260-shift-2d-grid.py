class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        arr = [x for row in grid for x in row]

        k %= len(arr)
        arr = arr[-k:] + arr[:-k]

        idx = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = arr[idx]
                idx += 1

        return grid