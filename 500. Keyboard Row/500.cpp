class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        set<char> row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'};
        set<char> row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'};
        set<char> row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'};
        vector<set<char>> rows = {row1, row2, row3};
        
        vector<string> ans;
        for (int i=0; i<words.size(); ++i){
            int row = 0;
            for (int j=0; j<rows.size(); ++j)
                row = (rows[j].count((char)tolower(words[i][0])) > 0) ? j : row;
            bool valid = true;
            for (int j=1; j<words[i].size(); ++j)
                if (rows[row].count((char)tolower(words[i][j])) == 0){
                    valid = false;
                    break;
                }
            if (valid) ans.push_back(words[i]);
        }
        return ans;
    }
};