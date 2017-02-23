class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        ans = []
        i=0
        j=0
        print nums1
        print nums2
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]: i+=1
            elif nums1[i] > nums2[j]: j+=1
            else:
                if len(ans) == 0 or nums1[i] != ans[-1]:
                    ans.append(nums1[i])
                i+=1
                j+=1
        return ans