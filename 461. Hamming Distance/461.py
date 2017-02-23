class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        val = x^y
        ct = 0
        while val:
            ct += 1 if val & 1 else 0
            val >>= 1
        return ct