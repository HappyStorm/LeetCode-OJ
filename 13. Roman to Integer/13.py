class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = self.roman(s[0])
        for i in range(1, len(s)):
            if self.roman(s[i]) > self.roman(s[i-1]):
                ans += self.roman(s[i]) - 2*self.roman(s[i-1])
            else: ans += self.roman(s[i])
        return ans
    
    def roman(self, c):
        if c == 'I': return 1
        elif c == 'V': return 5
        elif c == 'X': return 10
        elif c == 'L': return 50
        elif c == 'C': return 100
        elif c == 'D': return 500
        elif c == 'M': return 1000
        else: return 0
        