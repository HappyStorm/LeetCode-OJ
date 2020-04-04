class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nid = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[nid] = nums[nid], nums[i]
                nid += 1
