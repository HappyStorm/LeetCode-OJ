class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int col = matrix[0].size();
        int rs = 0, re = matrix.size()-1, rm = 0;
        while(rs <= re){
            rm = (rs+re)/2;
            if(matrix[rm][0] <= target && target <= matrix[rm][col-1])
                break;
            else if(matrix[rm][0] > target) re = rm-1;
            else rs = rm+1;
        }
        int cs = 0, ce = matrix[0].size()-1, cm = 0;
        while(cs <= ce){
            cm = (cs+ce)/2;
            if(matrix[rm][cm] > target) ce = cm-1;
            else if(matrix[rm][cm] < target) cs = cm+1;
            else return true;
        }
        return false;
    }
};
