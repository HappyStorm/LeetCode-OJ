class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        for n in nums:
            if cur < 2 or nums[cur-2] < n:
                nums[cur] = n
                cur += 1
        return cur
