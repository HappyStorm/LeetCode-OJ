class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows, cols = [0] * n, [0] * m
        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1

        ans = 0
        for i in range(n):
            for j in range(m):
               ans += 1 if rows[i] ^ cols[j] else 0

        return ans
