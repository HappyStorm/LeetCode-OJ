class Solution {
public:

    int minCostClimbingStairs(vector<int>& cost) {
        int top = cost.size();
        vector<int> dp(top, 0);
        dp[0] = cost[0]; dp[1] = cost[1];
        for(int i=2; i<top; ++i)
            dp[i] = cost[i] + min(dp[i-1], dp[i-2]);
        return min(dp[top-1], dp[top-2]);
    }
};
