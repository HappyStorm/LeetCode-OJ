class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        nrow, ncol = len(matrix), len(matrix[0])
        min_rows = set([min(row) for row in matrix])
        ans = []
        for col in range(ncol):
            max_col = matrix[0][col]
            for row in range(1, nrow):
                max_col = max(max_col, matrix[row][col])
            if max_col in min_rows:
                ans.append(max_col)
        return ans
