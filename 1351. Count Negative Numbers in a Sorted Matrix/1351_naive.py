class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ct = 0
        for row in grid:
            for v in row:
                if v < 0:
                    ct += 1

        return ct
