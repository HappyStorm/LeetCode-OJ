class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char, char> s2t, t2s;
        map<char, char>::iterator iter_s2t, iter_t2s;
        for(int i=0; i<s.length(); ++i){
            iter_s2t = s2t.find(s[i]);
            iter_t2s = t2s.find(t[i]);
            if(iter_s2t==s2t.end() && iter_t2s==t2s.end()){
                s2t.insert(pair<char, char>(s[i], t[i]));
                t2s.insert(pair<char, char>(t[i], s[i]));
            }
            else{
                if(iter_s2t->second != t[i] || iter_t2s->second != s[i])
                    return false;
            }
        }
        return true;
    }
};
