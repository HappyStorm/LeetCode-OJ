class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> ans;
        int i = 0, j = nums.size()-1;
        while (i<=j){
            int s = nums[i], e = nums[j];
            if(s<0) s = -s;
            if(e<0) e = -e;
            if (s<e){
                ans.push_back(pow(e, 2));
                j--;
            }
            else{
                ans.push_back(pow(s, 2));
                i++;
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
