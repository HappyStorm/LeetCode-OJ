class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans, nums = [], sorted(nums)
        cur, _sum = 0, sum(nums)
        while cur <= _sum:
            ans.append(nums.pop())
            cur += ans[-1]
            _sum -= ans[-1]
        return ans
