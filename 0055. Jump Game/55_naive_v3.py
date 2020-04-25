class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur, last, end = 0, 0, len(nums)
        for i in nums:
            last, cur = max(last, cur + i), cur + 1

            if cur > last:
                break

        return True if cur >= end else False