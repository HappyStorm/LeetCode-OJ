class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_dict = {n: i for i, n in enumerate(nums)}
        for i, n in enumerate(nums):
            com_idx = val_dict.get(target-n)
            if com_idx and i != com_idx:
                return [i, com_idx]
