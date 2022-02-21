class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ctmax, ctmap, hlen = 0, defaultdict(lambda: 0), len(nums)//2
        for i, n in enumerate(nums):
            ctmap[n] += 1
            if ctmap[n] > hlen:
                return n
            ctmax = max(ctmax, ctmap[n])
        return ctmax
