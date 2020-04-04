class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, tmp_sum, all_neg = 0, 0, True
        for n in nums:
            if n >= 0:
                all_neg = False
                tmp_sum += n

            else:
                if tmp_sum >= -n:
                    tmp_sum += n

                else:
                    tmp_sum = 0

            ans = max(ans, tmp_sum)

        return ans if not all_neg else max(nums)
