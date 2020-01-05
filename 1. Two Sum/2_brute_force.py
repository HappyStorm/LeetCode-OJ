class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            for ii, vv in enumerate(nums[i+1:]):
                if v+vv == target:
                    return [i, i+ii+1]