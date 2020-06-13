class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        dp = [[] for _ in range(len(nums)+1)]
        nums = sorted(nums)
        dp[0] = [nums[0]]
        for i in range(1, len(nums)):
            max_set = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) > len(max_set):
                        max_set = dp[j]

            dp[i] = max_set + [nums[i]]

        return max(dp, key=len)
