class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ans, cur = [], 0
        for i, c in enumerate(S):
            if c == C:
                ans += [d for d in range(cur, -1, -1)]
                cur = 0
            else:
                cur += 1
        if len(ans) != len(S):
            ans += [d for d in range(1, len(S) - len(ans)+1)]

        ans_reverse, cur = [], 0
        for i, c in enumerate(S[::-1]):
            if c == C:
                ans_reverse += [d for d in range(cur, -1, -1)]
                cur = 0
            else:
                cur += 1
        if len(ans_reverse) != len(S):
            ans_reverse += [d for d in range(1, len(S) - len(ans_reverse)+1)]

        return [min(i, j) for i, j in zip(ans, ans_reverse[::-1])]
