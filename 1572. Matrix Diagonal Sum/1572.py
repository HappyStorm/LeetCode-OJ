class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans, n = 0, len(mat)
        for i in range(n):
            f, b = i, n-i-1
            ans += (mat[f][f] + mat[b][f]) if f != b else mat[f][f]
        return ans
