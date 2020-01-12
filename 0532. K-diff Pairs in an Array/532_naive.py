class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0

        d = {}
        for n in nums:
            if d.get(n+k):
                d[n+k] += 1

            else:
                d[n+k] = 1

        ans = 0
        for n in nums:
            if d.get(n):
                if k:
                    d[n] = False
                    ans += 1
                else:
                    if d[n] >= 2:
                        d[n] = False
                        ans += 1

        return ans
