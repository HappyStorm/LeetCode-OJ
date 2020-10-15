class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = {}
        for i, v in enumerate(sorted(nums)):
            ans.setdefault(v, i)
        return [ans[n] for n in nums]
