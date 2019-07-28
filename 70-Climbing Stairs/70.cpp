class Solution {
public:
    int dp[10000]={0};
    int climbStairs(int n) {
        return (n>2) ? ((!dp[n]) ? dp[n] = climbStairs(n-1) + climbStairs(n-2) : dp[n]) : ((n==1) ? dp[1]=1 : dp[2]=2);
    }
};