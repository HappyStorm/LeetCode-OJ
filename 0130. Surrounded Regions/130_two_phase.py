class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row, col = len(board), len(board[0])
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        queue = [(r, c) for c in range(col) for r in range(row)
                 if (r in [0, row-1] or c in [0, col-1]) and board[r][c]=='O']

        while queue:
            r, c = queue.pop()
            if board[r][c] == 'O':
                board[r][c] = 'N'
                queue += [(r+mr, c+mc) for mr, mc in moves if 0 <= r+mr < row and 0 <= c+mc < col]

        board[:] = [['XO'[board[r][c] == 'N'] for c in range(col)] for r in range(row)]
