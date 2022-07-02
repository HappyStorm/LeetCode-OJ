class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = 0, sub_sum = 0, max_n = nums[0];
        bool all_neg = true;
        for(auto const &n: nums){
            if(n>=0){
                all_neg = false;
                sub_sum += n;
            }
            else{
                if(sub_sum >= -n)
                    sub_sum += n;
                else
                    sub_sum = 0;
            }
            ans = max(ans, sub_sum);
            max_n = max(max_n, n);

        }
        return !all_neg ? ans : max_n;
    }
};
