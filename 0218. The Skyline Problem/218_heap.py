class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        boarders = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, 0) for _, R, _ in buildings}))
        ans, cur = [[0, 0]], [(0, float('inf'))]
        for L, nH, R in boarders:
            if nH:
                heapq.heappush(cur, (nH, R))

            while cur[0][1] <= L:
                heapq.heappop(cur)

            if ans and ans[-1][1] != -cur[0][0]:
                ans.append([L, -cur[0][0]])

        return ans[1:]
