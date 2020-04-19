class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not len(grid):
            return 0

        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if i==0 and j==0:
                    continue

                elif i==0 and j>0:
                    grid[i][j] += grid[i][j-1]

                elif i>0 and j==0:
                    grid[i][j] += grid[i-1][j]

                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])

        return grid[-1][-1]
