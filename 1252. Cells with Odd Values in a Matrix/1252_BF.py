class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat = [[0 for _ in range(m)] for i in range(n)]
        for r, c in indices:
            mat[r] = list(map(lambda x: x+1, mat[r]))

            for i in range(n):
                mat[i][c] +=1

        ans = 0
        for i in range(n):
            for j in range(m):
               ans += 1 if mat[i][j] % 2 else 0
        return ans
