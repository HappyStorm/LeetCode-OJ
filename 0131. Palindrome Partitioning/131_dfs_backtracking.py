class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []

        def dfs(s, start, current):
            if start >= len(s):
                self.ans.append(current)
            for end in range(start, len(s)):
                if self.isPalindrome(s[start:end+1]):
                    dfs(s, end+1, current+[s[start:end+1]])
        dfs(s, 0, [])
        return self.ans

    def isPalindrome(self, s):
        _len = len(s)
        for i in range(_len):
            if s[i] != s[_len-1-i]:
                return False
        return True
