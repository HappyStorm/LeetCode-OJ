class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if dic.get(nums[i]) != None:
                return True
            else:
                dic[nums[i]] = 1;
        return False