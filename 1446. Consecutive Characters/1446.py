class Solution:
    def maxPower(self, s: str) -> int:
        ans, ct, char = 0, 1, None
        for c in s:
            if c == char:
                ct += 1
            else:
                ans = max(ans, ct)
                ct, char = 1, c

        return max(ans, ct)
