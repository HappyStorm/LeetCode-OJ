class Solution:
    def maxPower(self, s: str) -> int:
        ans, ct, char = 0, 1, None
        for c in s:
            if c == char:
                ct += 1
            else:
                ct, char = 1, c
                ans = max(ans, ct)

        return max(ans, ct)
