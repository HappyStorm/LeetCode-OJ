class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int slen = s.length(), plen = p.length();
        if(plen>slen) return {};

        vector<int> ans, tar(26, 0), win(26, 0);
        for(int i=0; i<plen; ++i){
            tar[p[i]-'a']++;
            win[s[i]-'a']++;
        }
        if(win==tar) ans.push_back(0);
        for(int i=plen; i<slen; ++i){
            win[s[i-plen]-'a']--;
            win[s[i]-'a']++;
            if(win==tar) ans.push_back(i-plen+1);
        }
        return ans;
    }
};
