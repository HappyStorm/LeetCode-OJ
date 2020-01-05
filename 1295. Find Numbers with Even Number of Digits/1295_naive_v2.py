class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            if not len(str(n)) % 2:
                ans += 1

        return ans