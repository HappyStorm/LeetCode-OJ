class StockSpanner:

    def __init__(self):
        self.stocks = []
        self.spans = []
        self.days = 0

    def next(self, price: int) -> int:
        self.stocks += [price]
        self.days += 1

        if self.days == 1:
            self.spans += [(1, 0)]
            return 1

        ans, max_day_id, pre_day_id = 1, self.days-2, self.days-1
        while max_day_id >= 0:

            if price >= self.stocks[max_day_id]:
                day_bound_stock = self.stocks[self.spans[max_day_id][1]]

                if price >= day_bound_stock and self.stocks[max_day_id] >= day_bound_stock:
                    ans += self.spans[max_day_id][0]
                    self.spans += [(ans, pre_day_id)]
                    return ans

                elif price >= day_bound_stock and self.stocks[max_day_id] < day_bound_stock:
                    ans += self.spans[max_day_id][0]
                    pre_day_id = max_day_id
                    max_day_id = self.spans[max_day_id][1]
                    continue

                else:
                    ans += self.spans[max_day_id][0]
                    self.spans += [(ans, self.spans[max_day_id][1])]
                    return ans

            else:
                self.spans += [(ans, max_day_id)]
                return ans




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
