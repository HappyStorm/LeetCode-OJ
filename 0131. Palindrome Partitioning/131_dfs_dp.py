class Solution:
    def partition(self, s: str) -> List[List[str]]:
        _len = len(s)
        self.ans, self.dp = [], [
            [False for _ in range(_len)] for _ in range(_len)]

        def dfs(s, start, current):
            if start >= len(s):
                self.ans.append(current)
            for end in range(start, len(s)):
                if s[start] == s[end] and (end-start <= 2 or self.dp[start+1][end-1]):
                    self.dp[start][end] = True
                    dfs(s, end+1, current+[s[start:end+1]])
        dfs(s, 0, [])
        return self.ans

    def isPalindrome(self, s):
        return s == s[::-1]
