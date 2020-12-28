class Solution:
    def reachNumber(self, target):
        target = abs(target)
        n = int(math.ceil(math.sqrt(1 + (target << 3))/2 - 0.5))
        mod = target % 2
        while mod != n*(n+1)/2 % 2:
            n += 1
        return n
