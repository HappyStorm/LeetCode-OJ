class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        if(image[sr][sc]==color) return image;

        queue<pair<int, int>> que;
        int m = image.size(), n = image[0].size();
        int oldColor = image[sr][sc];

        que.push({sr, sc});
        while(!que.empty()){
            auto pts = que.front();
            que.pop();

            int r = pts.first, c = pts.second;
            image[r][c] = color;
            if(c-1>=0 && image[r][c-1]==oldColor)
                que.push({r, c-1});
            if(c+1<n && image[r][c+1]==oldColor)
                que.push({r, c+1});
            if(r-1>=0 && image[r-1][c]==oldColor)
                que.push({r-1, c});
            if(r+1<m && image[r+1][c]==oldColor)
                que.push({r+1, c});
        }
        return image;
    }
};
