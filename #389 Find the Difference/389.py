class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = ord(t[0])
        for i in range(len(s)):
            ans ^= ord(s[i])
        for i in range(1, len(t)):
            ans ^= ord(t[i])
        return chr(ans)