class Solution {
public:
    vector<int> constructRectangle(int area) {
        vector<int> ans;
        int L = area;
        for (int i=int(sqrt(area)); i>0; --i){
            if (!(area%i)) {
                L = (i>area/i) ? i : area/i;
                break;
            }
        }
        ans.push_back(L), ans.push_back(area/L);
        return ans;
    }
};