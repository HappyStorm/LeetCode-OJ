class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans, ct = 0, 0
        for c in s:
            ct += 1 if c=='L' else -1
            ans += 0 if ct else 1

        return ans