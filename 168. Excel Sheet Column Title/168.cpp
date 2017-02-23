class Solution {
public:
    string convertToTitle(int n) {
        string s;
        while(n>0){
            int r = n%26;
            if(r) s.push_back(r+'A'-1);
            else s.push_back('Z'), n--;
            n /= 26;
        }
        std::reverse(s.begin(), s.end());
        return s;
    }
};