class Solution:
    def getsum(self, n):
        _sum = 0
        for s in str(n):
            _sum += int(s)**2

        return _sum

    def isHappy(self, n: int) -> bool:
        cur = n
        nlist = []
        while True:
            nlist += [cur]
            cur = self.getsum(cur)

            if cur == 1:
                return True

            if cur in nlist:
                return False
