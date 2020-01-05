class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        N = len(board)

        for i in range(N):
            for j in range(N):
                if board[i][j] == 'R':
                    rook_rid = j
                    rook_cid = i

        rook_row = board[rook_cid]
        rook_col = [row[rook_rid] for row in board]

        ans = 0
        B_min, B_max = 0, N
        for i, v in enumerate(rook_row):
            if v == 'B':
                if i < rook_rid:
                    B_min = i

                else:
                    B_max = i

        p_min, p_max = 0, 0
        for i, v in enumerate(rook_row):
            if v == 'p':
                if i<rook_rid and i>B_min:
                    p_min = 1

                elif i>rook_rid and i<B_max:
                    p_max = 1

        ans += p_min + p_max

        B_min, B_max = 0, N
        for i, v in enumerate(rook_col):
            if v == 'B':
                if i < rook_cid:
                    B_min = i

                else:
                    B_max = i

        p_min, p_max = 0, 0
        for i, v in enumerate(rook_col):
            if v == 'p':
                if i<rook_cid and i>B_min:
                    p_min = 1

                elif i>rook_cid and i<B_max:
                    p_max = 1

        ans += p_min + p_max

        return ans
