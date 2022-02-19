class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for n in nums:
            pq.append(-2*n if n & 1 else -n)
        ans, nvmax = float('inf'), max(pq)
        heapify(pq)
        while pq:
            nvmin = heappop(pq)
            ans = min(ans, nvmax-nvmin)
            if nvmin & 1:
                break
            nvmin >>= 1
            nvmax = max(nvmax, nvmin)
            heappush(pq, nvmin)
        return ans
