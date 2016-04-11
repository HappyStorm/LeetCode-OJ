class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        while n>0:
            r = n%26
            if r!=0: ans += chr(r+ord('A')-1)
            else:
                ans += 'Z'
                n -= 1
            n /= 26
        return ans[::-1]