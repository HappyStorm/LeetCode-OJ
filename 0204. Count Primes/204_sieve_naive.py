class Solution:
    prime_table = []

    def buildPrimeTable(self, n):
        self.prime_table = [True] * n
        for i in range(2, n):
            if i * i >= n:
                break

            if self.prime_table[i]:
                for j in range(i*i, n, i):
                    self.prime_table[j] = False

    def countPrimes(self, n: int) -> int:
        self.buildPrimeTable(n)
        ans = sum(self.prime_table) - 2
        return ans if ans > 0 else 0