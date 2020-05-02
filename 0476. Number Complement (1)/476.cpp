class Solution {
public:
    int findComplement(int num) {
        int ans = num&1^1, pow=0;
        while (num>>=1)
            ans += (num&1^1)<<++pow;
        return ans;
    }
};