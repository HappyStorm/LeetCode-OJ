class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int i=0, j=0;
        vector<int> ans;
        std::sort(nums1.begin(), nums1.end()), std::sort(nums2.begin(), nums2.end());
        while (i<nums1.size() && j<nums2.size()){
            if (nums1[i] < nums2[j]) ++i;
            else if (nums1[i] > nums2[j]) ++j;
            else {
                if (ans.size() == 0 || nums1[i] != ans.back())
                    ans.push_back(nums1[i]);
                ++i, ++j;
            }
        }
        return ans;
    }
};