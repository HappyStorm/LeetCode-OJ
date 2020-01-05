class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([i for i in nums if not len(str(i)) % 2])