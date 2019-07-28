class Solution(object):

    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for e in findNums:
            start = nums.index(e)
            find = False
            for i in range(start, len(nums)):
                if nums[i] > e:
                    ans += [nums[i]]
                    find = True
                    break
            if not find:
                ans += [-1]
        return ans
