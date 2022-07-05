class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0, min_price = INT_MAX;
        for(auto &p: prices){
            if(p < min_price)
                min_price = p;
            profit = max(profit, p - min_price);
        }
        return profit;
    }
};
