class Solution {
public:
    int getSum(int a, int b) {
        int cxor = a^b, cand = a&b;
        return (cand==0) ? cxor : getSum(cxor, cand<<1);
    }
};