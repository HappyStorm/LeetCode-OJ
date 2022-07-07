class Solution {
public:
    int firstUniqChar(string s) {
        int ans = INT_MAX, arr[26];
        fill_n(arr, 26, -1);
        for(int i=0; i<s.length(); ++i){
            if(arr[s[i]-'a']>=0)
                arr[s[i]-'a'] = -2;
            else
                if(arr[s[i]-'a']!=-2)
                    arr[s[i]-'a'] = i;
        }
        for(auto& i: arr)
            if(i>=0) ans = min(ans, i);
        return ans >= s.length() ? -1 : ans;
    }
};
