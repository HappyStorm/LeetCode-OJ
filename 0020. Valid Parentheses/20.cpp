class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for(auto& c: s){
            if(stk.empty()){
                if(c==')' || c==']' || c=='}') return false;
                stk.push(c);
            }
            else{
                if(c==')' || c==']' || c=='}'){
                    char top = stk.top();
                    if(c==')'){
                        if(top!='(') return false;
                        stk.pop();
                    }
                    else if(c==']'){
                        if(top!='[') return false;
                        stk.pop();
                    }
                    else{
                        if(top!='{') return false;
                        stk.pop();
                    }
                }
                else
                    stk.push(c);
            }
        }
        return stk.empty();
    }
};
