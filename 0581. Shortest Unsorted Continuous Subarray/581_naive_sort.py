class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        st_idx, ed_idx, flag = 0, 0, False
        sort_nums = sorted(nums)

        for i in range(len(nums)):
            if not flag:
                if sort_nums[i] != nums[i]:
                    st_idx = i
                    flag = True

            else:
                if sort_nums[i] != nums[i]:
                    ed_idx = i

        return ed_idx - st_idx + 1 if flag else 0
