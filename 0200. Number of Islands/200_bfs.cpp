class Solution {
public:
    struct pts{
        int r;
        int c;
    };
    int numIslands(vector<vector<char>>& grid) {
        queue<pts> que;
        int nIslands = 0;
        int m = grid.size(), n = grid[0].size();
        const vector<vector<int>> dirs = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                if(grid[i][j]=='1'){
                    nIslands++;
                    que.push({i, j});
                    grid[i][j] = '0';
                    while(!que.empty()){
                        pts p = que.front();
                        que.pop();
                        for(auto& dir: dirs){
                            int nr = p.r + dir[0], nc = p.c + dir[1];
                            if(nr<0 || nr>=m || nc<0 || nc>=n) continue;
                            if(grid[nr][nc]=='1'){
                                que.push({nr, nc});
                                grid[nr][nc] = '0';
                            }
                        }
                    }
                }
            }
        }
        return nIslands;
    }
};
