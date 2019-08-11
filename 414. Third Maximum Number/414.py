class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)

        ct, _max = 2, max(nums)
        while ct:
            nums.remove(_max)
            if len(nums) == 0:
                return _max

            _max = max(nums)
            ct -= 1

        return _max