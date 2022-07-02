class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> nset;
        for(auto i: nums){
            if(nset.find(i)!=nset.end()) return true;
            else nset.insert(i);
        }
        return false;
    }
};
