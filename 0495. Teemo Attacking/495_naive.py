class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not len(timeSeries):
            return 0

        pt = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i + 1] >= timeSeries[i] + duration:
                pt += duration

            else:
                pt += timeSeries[i + 1] - timeSeries[i]

        return pt + duration
