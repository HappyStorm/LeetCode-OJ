class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_end = max_ans = nums[0]
        for n in nums[1:]:
            max_end = max(n, max_end + n)
            max_ans = max(max_ans, max_end)

        return max_ans
