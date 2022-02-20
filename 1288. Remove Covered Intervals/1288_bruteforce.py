class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = _len = len(intervals)
        imap = defaultdict(lambda: None)
        for i in range(_len):
            a = intervals[i][0]
            b = intervals[i][1]
            if imap[(a, b)] is None:
                imap[(a, b)] = True
            for j in range(i+1, _len):
                c = intervals[j][0]
                d = intervals[j][1]
                if imap[(c, d)] is None:
                    imap[(c, d)] = True
                if c <= a and b <= d and imap.get((a, b), False):
                    ans -= 1
                    imap[(a, b)] = False
                if a <= c and d <= b and imap.get((c, d), False):
                    ans -= 1
                    imap[(c, d)] = False
        return ans
