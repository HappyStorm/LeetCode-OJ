class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = 1 << 31
        nums = list(map(lambda x: 0 if x < 0 else x, nums))
        for i in nums:
            if (i & ~mask) >= 1 and i & ~mask <= len(nums):
                nums[(i & ~mask) - 1] |= mask
        for i in nums:
            if not(i >> 31 & 1):
                return nums.index(i) + 1
        return len(nums) + 1
