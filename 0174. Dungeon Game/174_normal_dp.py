class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon), len(dungeon[0])
        hmap = [[sys.maxsize for _ in range(col+1)] for _ in range(row+1)]
        moves = [(-1, 0), (0, -1)]
        hmap[row][col-1] = hmap[row-1][col] = 1
        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                min_health = min(hmap[r+1][c], hmap[r][c+1]) - dungeon[r][c]
                hmap[r][c] = max(min_health, 1)

        return hmap[0][0]
