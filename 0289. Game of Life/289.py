class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        move = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)]
        for i in range(m):
            for j in range(n):
                count = 0
                for mr, mc in move:
                    ni, nj = i+mr, j+mc
                    if (0 <= ni < m) and (0 <= nj < n) and 1 <= board[ni][nj] <= 2:
                        count += 1

                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == 3:
                    board[i][j] = 1
