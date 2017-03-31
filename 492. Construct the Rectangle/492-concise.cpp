class Solution {
public:
    vector<int> constructRectangle(int area) {
        vector<int> ans;
        int L = int(sqrt(area));
        while (area%L) --L;
        ans.push_back(area/L), ans.push_back(L);
        return ans;
    }
};