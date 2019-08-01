class RecentCounter:

    def __init__(self):
        self.pq = collections.deque()

    def ping(self, t: int) -> int:
        self.pq.append(t)
        while self.pq[0] < t-3000:
            self.pq.popleft()

        return len(self.pq)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)