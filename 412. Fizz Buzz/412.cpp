class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> ans;
        string temp;
        for(int i=1; i<=n; ++i){
              temp = (i%3!=0 && i%5!=0) ? to_string(i) :
                     ((i%3==0 && i%5!=0) ? string("Fizz") :
                     (((i%3!=0 && i%5==0) ? string("Buzz") : string("FizzBuzz"))));
            ans.push_back(temp);
        }
        return ans;
    }
    
};