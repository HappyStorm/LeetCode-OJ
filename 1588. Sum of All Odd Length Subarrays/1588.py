class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans, _len = 0, len(arr)
        for i, v in enumerate(arr):
            ans += ((i+1) * (_len-i) + 1) // 2 * v
        return ans
