class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ct_dict, ct, ans = {0: 0}, 0, 0
        for i, v in enumerate(nums, 1):
            ct += 1 if v else -1

            if ct in ct_dict:
                ans = max(ans, i - ct_dict[ct])

            else:
                ct_dict[ct] = i

        return ans
