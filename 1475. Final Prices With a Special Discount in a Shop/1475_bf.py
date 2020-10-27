class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i, price in enumerate(prices):
            is_discount = False
            for j, discount in enumerate(prices[i+1:]):
                if discount <= price:
                    ans.append(price-discount)
                    is_discount = True
                    break
            if not is_discount:
                ans.append(price)
        return ans
