class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = nums[0]
        for n in nums[1:]:
            ans ^= n

        return ans
