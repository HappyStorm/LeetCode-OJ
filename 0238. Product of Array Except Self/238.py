class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L, R = len(nums) * [1], len(nums) * [1]
        for i in range(1, len(nums)):
            L[i] = L[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]

        ans = []
        for i in range(len(nums)):
            ans += [L[i]*R[i]]

        return ans
