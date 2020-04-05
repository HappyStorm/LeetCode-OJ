class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nid = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[nid] = nums[i]
                nid += 1

        for i in range(nid, len(nums)):
            nums[i] = 0
