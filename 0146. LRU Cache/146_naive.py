class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.age = {}
        self.cur_age = 0
        self.min_age = 0

    def get(self, key: int) -> int:
        res = self.cache.get(key)
        if res is not None:
            del self.age[res[1]]
            self.cache[key][1] = self.cur_age
            self.age[self.cur_age] = key
            self.cur_age += 1

            while self.age.get(self.min_age) is None:
                self.min_age += 1

            return res[0]

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key) is not None:
            del self.age[self.cache[key][1]]

        else:
            if self.capacity > 0:
                self.capacity -= 1

            else:
                del self.cache[self.age[self.min_age]]
                del self.age[self.min_age]

        self.cache[key] = [value, self.cur_age]
        self.age[self.cur_age] = key
        self.cur_age += 1

        while self.age.get(self.min_age) is None:
            self.min_age += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
