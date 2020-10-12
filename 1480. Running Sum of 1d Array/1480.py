class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans, ct = [], 0
        for n in nums:
            ct += n
            ans.append(ct)
        return ans
