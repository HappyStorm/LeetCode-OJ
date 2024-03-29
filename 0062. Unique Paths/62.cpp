class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp;
        for(int i=0; i<m; ++i)
            dp.push_back(vector<int>(n, 0));

        dp[0][0] = 1;
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                if(i==0 && j==0) continue;
                else if(i==0 && j>=1)
                    dp[i][j] = 1;
                else if(i>=1 && j==0)
                    dp[i][j] = 1;
                else
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};
