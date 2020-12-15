class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans, st, ed = [], 0, len(nums)-1
        while st <= ed:
            if abs(nums[st]) >= abs(nums[ed]):
                ans.append(nums[st]**2)
                st += 1
            else:
                ans.append(nums[ed]**2)
                ed -= 1
        return ans[::-1]
