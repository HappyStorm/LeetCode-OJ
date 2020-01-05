class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ans = 0, ct = 0;
        for(int i=0; i<nums.size(); ++i)
            if (nums[i]) ans = (++ct > ans) ? ct : ans;
            else ct = 0;
        return ans;
    }
};