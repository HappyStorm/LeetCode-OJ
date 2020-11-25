class Solution:
    def average(self, salary: List[int]) -> float:
        ssum, smin, smax = 0, sys.float_info.max, sys.float_info.min
        for s in salary:
            ssum += s
            smin = min(smin, s)
            smax = max(smax, s)
        return (ssum - smin - smax) / (len(salary)-2)
