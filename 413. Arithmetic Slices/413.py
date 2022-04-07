class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        ans, diff, tmp, = 0, nums[1]-nums[0], [nums[0], nums[1]]
        for i, v in enumerate(nums[2:]):
            if v-tmp[-1] == diff:
                tmp.append(v)
            else:
                tmp_len = len(tmp)
                if tmp_len >= 3:
                    ans += (tmp_len-2) * (tmp_len-1) // 2
                diff = v - tmp[-1]
                tmp = [tmp[-1], v]

        tmp_len = len(tmp)
        if len(tmp) >= 3:
            ans += (len(tmp)-2) * (len(tmp)-1) // 2
        return ans
