class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = [0]*n
        k -= n
        cur = n-1
        while k > 0:
            res = min(k, 25)
            ans[cur] += res
            k -= res
            cur -= 1
        return ''.join(map(lambda x: chr(x+ord('a')), ans))
