class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i, j in zip(range(len(s)-1, -1, -1), range(len(s))):
            ans += (ord(s[i]) - ord('A') + 1) * pow(26, j)
        return ans