class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        len_a, len_b = len(A), len(B)
        dp = [[0 for _ in range(len_b+1)] for _ in range(len_a+1)]
        for i in range(len_a):
            for j in range(len_b):
                dp[i+1][j+1] = 1 + dp[i][j] if A[i] == B[j] else max(dp[i][j + 1], dp[i + 1][j])

        return dp[-1][-1]
