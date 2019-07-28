class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        vector<int> ans;
        for(int i=0; i<findNums.size(); ++i){
            ptrdiff_t pos = find(nums.begin(), nums.end(), findNums[i]) - nums.begin();
            bool find = false;
            for(int j=pos; j<nums.size(); ++j){
                if(nums[j]>findNums[i]){
                    ans.push_back(nums[j]);
                    find = true;
                    break;
                }
            }
            if(!find) ans.push_back(-1);
        }
        return ans;
    }
};