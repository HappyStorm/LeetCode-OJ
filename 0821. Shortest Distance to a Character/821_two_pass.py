class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n, cur = len(S), float('inf')
        ans = [n] * n
        for i in range(n):
            if S[i] == C:
                cur = i
            ans[i] = min(ans[i], abs(i-cur))

        for i in range(n)[::-1]:
            if S[i] == C:
                cur = i
            ans[i] = min(ans[i], abs(i-cur))

        return ans
