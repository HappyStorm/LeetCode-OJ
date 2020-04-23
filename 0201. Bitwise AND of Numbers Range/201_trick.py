class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        ct = 0
        while m != n:
            m >>= 1
            n >>= 1
            ct += 1

        return m << ct
