class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::map<int, int> map;
        std::map<int, int>::iterator itr;
        for(int i=0; i<nums.size(); ++i){
            itr = map.find(nums[i]);
            if(itr==map.end())
                map.insert(std::pair<int, int>(nums[i], 1));
            else
                itr->second += 1;
        }
        itr = map.begin();
        int ct = 0, ans;
        for(; itr!=map.end(); itr++)
            if(itr->second >= (nums.size()/2))
                if(itr->second >= ct)
                    ans = itr->first, ct = itr->second;
        return ans;
    }
};