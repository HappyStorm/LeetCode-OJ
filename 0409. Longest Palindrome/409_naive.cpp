class Solution {
public:
    int longestPalindrome(string s) {
        int upper[26] = {0}, lower[26] = {0};
        for(const auto& c: s){
            if(c>='a')
                lower[c-'a']++;
            else
                upper[c-'A']++;
        }

        int ans = 0;
        bool odd = false;
        for(int i=0; i<26; ++i){
            if(upper[i]%2==0)
                ans += upper[i];
            else{
                odd = true;
                if(upper[i]>1)
                    ans += (upper[i]-1);
            }
            if(lower[i]%2==0)
                ans += lower[i];
            else{
                odd = true;
                if(lower[i]>1)
                    ans += (lower[i]-1);
            }
        }
        return odd ? ans+1 : ans;
    }
};
