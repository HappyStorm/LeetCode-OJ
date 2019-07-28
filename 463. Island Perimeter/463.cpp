class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int ans = 0;
        vector<int> row;
        for (int i=0; i<grid.size(); ++i){
            row.clear();
            row.push_back(0);
            for (int j=0; j<grid[i].size(); ++j)
                row.push_back(grid[i][j]);
            row.push_back(0);
            for (int j=1; j<row.size(); ++j)
                ans += (row[j] != row[j-1]) ? 1 : 0;
        }
        for (int j=0; j<grid[0].size(); ++j){
            row.clear();
            row.push_back(0);
            for (int i=0; i<grid.size(); ++i)
                row.push_back(grid[i][j]);
            row.push_back(0);
            for (int i=1; i<row.size(); ++i)
                ans += (row[i] != row[i-1]) ? 1 : 0;
        }
        return ans;
    }
};