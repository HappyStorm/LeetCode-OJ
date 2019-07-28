class Solution {
public:
    bool canJump(vector<int>& nums) {
        int r;
        nums[0] |= ~INT_MAX;
        for (int i=0; i<nums.size(); ++i){
            r = nums[i]&INT_MAX;
            if ((nums[i]>>31)&1)
                for (int j=i; j<=i+r && j<nums.size(); ++j)
                    nums[j] |= ~INT_MAX;
        }
        return ((nums[nums.size()-1]>>31)&1) ? true : false;
    }
};