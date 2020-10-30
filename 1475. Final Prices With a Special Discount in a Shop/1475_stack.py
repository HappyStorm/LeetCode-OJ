class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans, stk = prices[:], []
        for i, price in enumerate(prices):
            while stk and prices[stk[-1]] >= price:
                ans[stk.pop()] -= price
            stk.append(i)
        return ans
