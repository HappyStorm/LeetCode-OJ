class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = dp[1] = 1
        for i in range(2, len(s)+1):
            if '1' <= s[i-1] <= '9':
                dp[i] += dp[i-1]
            if (s[i-2] == '1' and '0' <= s[i-1] <= '9') or\
               (s[i-2] == '2' and '0' <= s[i-1] <= '6'):
                dp[i] += dp[i-2]
        return dp[len(s)]
