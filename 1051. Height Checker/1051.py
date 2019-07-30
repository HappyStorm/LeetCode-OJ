class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = sorted(heights)
        ct = 0
        for i in range(len(ans)):
            if heights[i] != ans[i]:
                ct += 1

        return ct