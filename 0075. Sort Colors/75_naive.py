class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ct0 = ct1 = ct2 = 0
        for n in nums:
            if n == 0:
                ct0 += 1

            elif n == 1:
                ct1 += 1

            elif n == 2:
                ct2 += 1

            else:
                continue

        ct = 0
        while ct0 > 0 or ct1 > 0 or ct2 > 0:
            if ct0 > 0:
                nums[ct] = 0
                ct += 1
                ct0 -= 1

            elif ct1 > 0:
                nums[ct] = 1
                ct += 1
                ct1 -= 1

            elif ct2 > 0:
                nums[ct] = 2
                ct += 1
                ct2 -= 1
