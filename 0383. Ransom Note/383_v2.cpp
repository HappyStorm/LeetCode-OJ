class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int quota[26] = {0};
        for(const auto& c: magazine)
            quota[c-'a']++;
        for(const auto& c: ransomNote){
            quota[c-'a']--;
            if(quota[c-'a']<0) return false;
        }
        return true;
    }
};
