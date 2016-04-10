class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        ls = [0] * 26
        lt = [0] * 26
        for i in range(len(s)):
            ls[ord(s[i])-ord('a')] += 1
            lt[ord(t[i])-ord('a')] += 1
        for i in range(26):
            if ls[i] != lt[i]: return False
        return True