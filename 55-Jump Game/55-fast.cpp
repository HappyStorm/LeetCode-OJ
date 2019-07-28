class Solution {
public:
    bool canJump(vector<int>& nums) {
        int cur = 0;
        for (int last=0; cur<nums.size() && cur<=last; ++cur)
            last = max(last, cur+nums[cur]);
        return (cur==nums.size()) ? true : false;
    }
};