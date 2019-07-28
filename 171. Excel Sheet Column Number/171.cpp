class Solution {
public:
    int titleToNumber(string s) {
        int ans = 0;
        std::reverse(s.begin(), s.end());
        for(int i=0; i<s.length(); ++i)
            ans += (s[i]-'A'+1) * pow(26, i);
        return ans;
    }
};