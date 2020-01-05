class RecentCounter:

    def __init__(self):
        self.plist = []
        self.id = 0
        self.ct = 0

    def ping(self, t: int) -> int:
        self.plist += [t]
        self.ct += 1

        while self.plist[self.id] < t - 3000:
            self.id += 1
            self.ct -= 1

        return self.ct



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)