class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int charset[26+5] = {0};
        for (int i=0; i<magazine.size(); ++i)
            ++charset[magazine[i]-'a'];
        for (int i=0; i<ransomNote.size(); ++i)
            if (!charset[ransomNote[i]-'a']--)
                return false;
        return true;
    }
};