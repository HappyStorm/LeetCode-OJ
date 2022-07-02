class Solution {
public:
    bool isSubsequence(string s, string t) {
        size_t ct_s = 0, ct_t = 0;
        size_t len_s = s.length(), len_t = t.length();
        while(ct_s < len_s and ct_t < len_t){
            if(s.at(ct_s) != t.at(ct_t)){
                ct_t++;
            }
            else{
                ct_s++;
                ct_t++;
            }
        }
        return true ? ct_s == len_s : false;
    }
};
