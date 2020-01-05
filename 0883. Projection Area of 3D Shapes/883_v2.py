class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        ans = 0

        for i in range(N):
            max_xz, max_yz = 0, 0
            for j in range(N):
                ans += 1 if grid[i][j] else 0
                max_xz = max(max_xz, grid[i][j])
                max_yz = max(max_yz, grid[j][i])

            ans += max_xz + max_yz

        return ans
