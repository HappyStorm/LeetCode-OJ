class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            if (target - n) in nums:
                ii = nums.index((target - n))
                if i != ii:
                    return [i , ii]
