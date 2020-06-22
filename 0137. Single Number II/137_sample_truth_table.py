class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lbs = hbs = 0
        for n in nums:
            lbs = ~hbs & (lbs ^ n)
            hbs = ~lbs & (hbs ^ n)
        return lbs
