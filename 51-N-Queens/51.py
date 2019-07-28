n = 4
ans = []


def valid(board, n):
    rows = [r for r in board]
    cols = list(map(list, zip(*rows)))
    return False if any([sum(r) > 1 for r in rows] + [sum(c) > 1 for c in cols]) \
                    or any([sum([board[i + k][k] for k in range(n) if i + k < n]) > 1 for i in range(n)]) \
                    or any([sum([board[k][j + k] for k in range(n) if j + k < n]) > 1 for j in range(n)]) \
                    or any([sum([board[i + k][n - k - 1] for k in range(n) if i + k < n]) > 1 for i in range(n)]) \
                    or any([sum([board[k][n - j - k - 1] for k in range(n) if j + k < n]) > 1 for j in range(n)]) \
                    else True


def dfs(cur_col, board, n, ans):
    if cur_col == n:
        ans += [[''.join(['Q' if col else '.' for col in row]) for row in board]]
    else:
        for i in range(n):
            board[i][cur_col] = 1
            if valid(board, n):
                dfs(cur_col + 1, board, n, ans)
            board[i][cur_col] = 0


# tboard = [[0] * n for _ in range(n)]
# tboard[0][1] = 1
# tboard[1][3] = 1
# tboard[2][0] = 1
# tboard[3][2] = 1
# valid(tboard, n)
dfs(0, [[0]*n for _ in range(n)], n, ans)
print(ans)
# for i in range(n):
#     for k in range(n):
#         if i+k < n:
#             print((i+k, n-k-1))
#     print()
# for j in range(1, n):
#     for k in range(n):
#         if j + k < n:
#             print((k, n-j-1-k))
#     print()
# for i in range(n-1, -1, -1):
#     print(i)


# n = 4
# def under_attack(col, queens):
#     left = right = col
#     for r, c in reversed(queens):
#         left, right = left - 1, right + 1
#         if c in (left, col, right):
#             return True
#     return False


# def solve(n):
#     if n == 0:
#         return [[]]
#     smaller_solutions = solve(n - 1)
#     return [solution + [(n, i + 1)]
#             for i in range(n)
#             for solution in smaller_solutions
#             if not under_attack(i + 1, solution)]

# ans, game = [], []
# for answer in solve(n):
#     for i in range(n):
#         row = []
#         for j in range(n):
#             row += ['.'] if (i, j) not in answer else ['Q']
#         game += [(''.join(row))]
#     ans += [game]
# print(ans)


# [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
