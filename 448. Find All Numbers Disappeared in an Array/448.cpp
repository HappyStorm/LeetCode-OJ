class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> ans;
        for (int i=0; i<nums.size(); ++i)
            nums[(nums[i]&INT_MAX)-1]|= ~INT_MAX;
        for (int i=0; i<nums.size(); ++i)
            if (!(nums[i]>>31&1)) ans.push_back(i+1);
        return ans;
    }
};