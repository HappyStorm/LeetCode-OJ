class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_val_list, n_idx_list = [], []
        for i, n in enumerate(nums):
            n_val_list += [n]
            n_idx_list += [i]

        for i, n in enumerate(nums):
            if (target - n) in n_val_list:
                ii = n_idx_list[n_val_list.index(target - n)]
                if i != ii:
                    return [i , ii]
