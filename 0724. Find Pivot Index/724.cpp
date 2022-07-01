class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int asum=0, lsum=0;
        for(auto n: nums)
            asum += n;
        for(int i=0; i<nums.size(); ++i){
            if(asum-lsum-nums[i]==lsum)
                return i;
            lsum += nums[i];
        }
        return -1;
    }
};
