class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, cur_sum, sum_map = 0, 0, {0: 1}
        for n in nums:
            cur_sum += n
            ans += sum_map.get(cur_sum-k, 0)
            if sum_map.get(cur_sum, None):
                sum_map[cur_sum] += 1
            else:
                sum_map[cur_sum] = 1
        return ans
