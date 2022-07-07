class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length()) return false;
        int quota[26] = {0};
        for(const auto& c: s)
            quota[c-'a']++;
        for(const auto& c: t){
            quota[c-'a']--;
            if(quota[c-'a']<0) return false;
        }
        return true;
    }
};
