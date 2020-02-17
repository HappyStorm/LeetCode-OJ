class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        t = len(timeSeries)
        if t == 0:
            return 0

        pt = 0
        for i in range(t - 1):
            pt += min(timeSeries[i + 1] - timeSeries[i], duration)

        return pt + duration
