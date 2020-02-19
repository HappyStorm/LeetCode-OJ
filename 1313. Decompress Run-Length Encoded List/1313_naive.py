class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [e for l in [[nums[i + 1]] * nums[i] for i in range(0, len(nums), 2)] for e in l]
