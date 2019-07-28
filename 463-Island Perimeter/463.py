class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for row in grid:
            ex_row = [0] + row + [0]
            for i in range(len(row) + 1):
                ans += 1 if ex_row[i] is not ex_row[i + 1] else 0
        grid_t = map(list, (zip(*grid)))
        for row in grid_t:
            ex_row = [0] + row + [0]
            for i in range(len(row) + 1):
                ans += 1 if ex_row[i] is not ex_row[i + 1] else 0
        return ans
