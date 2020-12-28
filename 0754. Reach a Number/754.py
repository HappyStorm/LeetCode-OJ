class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = int(math.sqrt(target << 1))
        mul, mod = (n*(n+1))//2, target % 2
        while mul < target or mul % 2 != mod:
            n += 1
            mul = (n*(n+1))//2
        return n
