class Solution:

    def __init__(self, w: List[int]):
        self.arr = w
        for i in range(1 , len(w)):
            self.arr[i] = self.arr[i-1] + w[i]

        self.len = len(w)

    def pickIndex(self) -> int:
        seed = random.randint(1, self.arr[-1])
        l, r = 0, self.len - 1
        while l < r:
            mid = (l+r) // 2
            if seed <= self.arr[mid]:
                r = mid

            else:
                l = mid + 1

        return l
