class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        from functools import reduce

        nums = [int(i) for i in str(n)]
        return reduce(lambda x, y: x*y, nums) - sum(nums)