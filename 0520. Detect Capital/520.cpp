class Solution {
public:
    bool detectCapitalUse(string word) {
        int ct = 0;
        for (int i=0; i<word.size(); ++i)
            ct += (word[i]<'a') ? 1 : 0;
        return (!ct || ct==word.size()) ? true : ((ct==1 && word[0]<'a') ? true : false);
    }
};