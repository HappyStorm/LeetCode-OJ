class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1

        n, r = 1, 1
        while r % K:
            r = (r % K) * 10 + 1
            n += 1

        return n
