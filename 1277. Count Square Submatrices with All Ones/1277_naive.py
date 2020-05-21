class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans, row, col = 0, len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] and 0 < i < row and 0 < j < col:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1

                ans += matrix[i][j]

        return ans
