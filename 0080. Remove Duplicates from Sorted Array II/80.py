class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        _len, cur, move = len(nums), 0, 0
        while move < _len:
            n, freq = nums[move], 0
            while move < _len and nums[move] == n:
                freq += 1
                if freq <= 2:
                    nums[cur] = n
                    cur += 1
                move += 1
        return cur
