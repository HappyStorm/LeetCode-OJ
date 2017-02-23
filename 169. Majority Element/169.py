class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)):
            if dic.get(nums[i]) != None:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        ct = 0
        ans = 0
        for key in dic:
            t = dic[key]
            if t >= len(nums)/2:
                if t > ct:
                    ans = key
                    ct = t
        return ans