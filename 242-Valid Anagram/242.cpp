class Solution {
public:
    bool isAnagram(string s, string t) {
        int slen = s.length(), tlen = t.length();
        if (slen!=tlen) return false;
        int ls[26+5]={0}, lt[26+5]={0};
        for(int i=0; i<slen; ++i)
            ls[s[i]-'a']++, lt[t[i]-'a']++;
        for(int i=0; i<26; ++i)
            if(ls[i]!=lt[i]) return false;
        return true;
    }
};