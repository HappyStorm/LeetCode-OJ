class Solution(object):
    dp = [0] * 10000
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            self.dp[1] = 1
            return self.dp[1]
        elif n==2:
            self.dp[2] = 2
            return self.dp[2]
        else:
            if self.dp[n]==0:
                self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
                return self.dp[n]
            else: return self.dp[n]