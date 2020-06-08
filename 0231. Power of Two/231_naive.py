class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        ct = 0
        while n:
            ct += n % 2
            n >>= 1

            if ct > 1:
                return False

        return True
