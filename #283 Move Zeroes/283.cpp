class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for(int i=0, p=0; i<nums.size(); ++i, ++p){
            if(nums[p]==0){
                nums.push_back(0);
                nums.erase(nums.begin()+p);
                if(p<nums.size()-1)
                    if(nums[p]==0 || nums[p+1]!=0)
                        --p;
            }
        }
    }
};