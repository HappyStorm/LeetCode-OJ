class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[None for _ in range(n)] for _ in range(n)]
        matrix[0][0] = 1
        r, c, cd, val, end = 0, 0, 0, 2, n**2
        while val <= end:
            dr, dc = dirs[cd % 4]
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < n:
                if matrix[nr][nc]:
                    cd += 1
                    continue
                else:
                    matrix[nr][nc] = val
                    r, c = nr, nc
                    val += 1
            else:
                cd += 1
        return matrix
