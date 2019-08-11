class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ct, _max = k-1, max(nums)
        while ct:
            nums.remove(_max)
            if len(nums) == 0:
                return _max

            _max = max(nums)
            ct -= 1

        return _max