class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not len(grid):
            return 0

        moves = [(0, 1), (1, 0)]
        row, col = len(grid), len(grid[0])
        queue, visit = [(0, 0)], [[0] * col for i in range(row)]
        while queue:
            i, j = queue[-1]
            queue.pop()
            if i >= row or j >= col:
                continue

            if not visit[i][j]:
                for move in moves:
                    ti, tj = i + move[0], j + move[1]
                    if ti < row and tj < col and not visit[ti][tj]:
                        queue = [(ti, tj)] + queue

            if i == 0 and j == 0:
                visit[i][j] = 1
                continue

            elif i == 0:
                grid[i][j] += grid[i][j-1]

            elif j == 0:
                grid[i][j] += grid[i-1][j]

            else:
                if not visit[i][j]:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])

            visit[i][j] = 1

        return grid[row-1][col-1]
