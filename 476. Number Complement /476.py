class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans, pow = num&1^1, 0;
        while num>1:
            num >>= 1
            pow += 1
            ans += (num&1^1) << pow;
        return ans