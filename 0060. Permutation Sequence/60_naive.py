class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        candidates = [str(i) for i in range(1, n+1)]
        factorials = [1]
        ans = ""
        for i in range(1, n):
            factorials += [i*factorials[-1]]

        for i in range(n, 0, -1):
            factor = factorials[i-1]
            d = (k-1) // factor
            k -= factor*d
            ans += candidates[d]
            candidates.remove(candidates[d])
        return ans
