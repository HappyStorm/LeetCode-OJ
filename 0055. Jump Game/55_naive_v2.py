class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        cur_pos, walk, max_len, end_len = 1, nums[0], 0, len(nums)-1
        for i, v in enumerate(nums[:-1]):
            if walk == 0:
                break

            walk -= 1
            walk = max(walk, v)
            tmp_len = i + v
            max_len = max(max_len, tmp_len)
            if max_len >= end_len:
                return True

        return max_len >= end_len
