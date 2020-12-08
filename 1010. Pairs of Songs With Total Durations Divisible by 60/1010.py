class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans, m = 0, [0]*60
        for t in time:
            ans += m[(60 - t % 60) % 60]
            m[t%60] += 1
        return ans
