class Solution(object):

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mask = 1 << 31
        for i in nums:
            nums[(i & ~mask) - 1] |= mask
        return [i + 1 for i in range(len(nums)) if not(nums[i] >> 31 & 1)]
