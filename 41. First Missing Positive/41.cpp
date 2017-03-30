class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        for (int i=0; i<nums.size(); ++i) nums[i] = (nums[i]<0) ? 0 : nums[i];
        for (int i=0; i<nums.size(); ++i)
            if ((nums[i]&INT_MAX)>=1 && (nums[i]&INT_MAX)<=nums.size())
                nums[(nums[i]&INT_MAX)-1] |= INT_MIN;
        for (int i=0; i<nums.size(); ++i) if (!(nums[i]>>31&1)) return i+1;
        return nums.size()+1;
    }
};
