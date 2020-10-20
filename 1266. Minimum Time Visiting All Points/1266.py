class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)-1):
            x0, y0 = points[i][0], points[i][1]
            x1, y1 = points[i+1][0], points[i+1][1]
            ans += max(abs(x1-x0), abs(y1-y0))
        return ans
