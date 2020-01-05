class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        st_idx, ed_idx, min_n, max_n = 0, 0, float("inf"), -float("inf")
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                min_n = min([min_n, nums[i+1]])

        for i in range(len(nums)-1, 0, -1):
            if nums[i] < nums[i-1]:
                max_n = max([max_n, nums[i-1]])

        for i in range(len(nums)):
            if nums[i] > min_n:
                st_idx = i
                break

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < max_n:
                ed_idx = i
                break

        return ed_idx - st_idx + 1 if ed_idx > st_idx else 0