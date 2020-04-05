class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            tmp_profit = prices[i+1] - prices[i]
            if tmp_profit > 0:
                profit += tmp_profit
                
        return profit
            