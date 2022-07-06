class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> pascal = {{1}};
        for(int i=1; i<numRows; ++i){
            int ct = 0;
            vector<int> layer = {1};
            while(layer.size()<i)
                layer.push_back(pascal[i-1][ct] + pascal[i-1][++ct]);
            layer.push_back(1);
            pascal.push_back(layer);
        }
        return pascal;
    }
};
