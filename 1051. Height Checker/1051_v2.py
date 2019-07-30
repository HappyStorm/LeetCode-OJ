class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = sorted(heights)
        if heights == ans:
            return 0

        else:
            return len([i for i in range(len(heights)) if heights[i] != ans[i]])
