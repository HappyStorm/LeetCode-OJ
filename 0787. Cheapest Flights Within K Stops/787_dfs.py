class Solution:
    ans = sys.maxsize
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        costs = [[-1 for _ in range(n)] for _ in range(n)]
        for u, v, w in flights:
            costs[u][v] = w

        self.dfs(n, src, dst, K, costs, 0, -1)

        return self.ans if self.ans != sys.maxsize else -1

    def dfs(self, n, src, dst, K, costs, cost, stop):
        if stop > K:
            return

        if src == dst:
            self.ans = cost
            return

        for i in range(n):
            if cost + costs[src][i] > self.ans or costs[src][i] < 0:
                continue

            self.dfs(n, i, dst, K, costs, cost + costs[src][i], stop+1)
