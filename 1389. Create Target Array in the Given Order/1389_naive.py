class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [None] * len(nums)
        for i in range(len(nums)):
            prev = target[:index[i]]
            tail = target[index[i]:-1]
            target = prev + [nums[i]] + tail
        return target
