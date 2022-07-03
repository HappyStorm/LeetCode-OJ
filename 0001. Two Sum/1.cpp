class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        map<int, int> hash;
        map<int, int>::iterator iter;
        int start = 0;
        for(int i=0; i<nums.size(); ++i){
            iter = hash.find(nums[i]);
            if(iter==hash.end())
                hash.insert(pair<int, int>(target-nums[i], i));
            else{
                ans.push_back(iter->second);
                ans.push_back(i);
                break;
            }
        }
        return ans;
    }
};
