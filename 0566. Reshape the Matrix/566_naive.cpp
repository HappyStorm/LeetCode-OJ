class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        vector<vector<int>> ans;
        int mat_r = mat.size(), mat_c = mat[0].size();
        if(mat_r*mat_c != r*c) return mat;

        int count = 0;
        vector<int> row;
        for(int i=0; i<mat_r; ++i){
            for(int j=0; j<mat_c; ++j){
                if(count>=c){
                    ans.push_back(row);
                    row.clear();
                    count = 0;
                }
                row.push_back(mat[i][j]);
                count++;
            }
        }
        if(!row.empty()) ans.push_back(row);
        return ans;
    }
};
