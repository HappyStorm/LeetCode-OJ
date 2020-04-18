class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans, row, col = 0, len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue

                if grid[i][j] == '1':
                    ans += 1
                    queue = [(i, j)]
                    while queue:
                        ti, tj = queue[-1]
                        queue.pop()
                        if ti < 0 or ti >= row or tj < 0 or tj >= col or grid[ti][tj] != '1':
                            continue

                        grid[ti][tj] = '0'
                        for move in moves:
                            queue = [(ti + move[0], tj + move[1])] + queue

        return ans
