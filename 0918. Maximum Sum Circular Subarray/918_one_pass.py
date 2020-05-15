class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_sum, min_sum, _sum, max_end, min_end = A[0], A[0], 0, 0, 0
        for n in A:
            max_end = max(n, max_end + n)
            max_sum = max(max_sum, max_end)

            min_end = min(n, min_end + n)
            min_sum = min(min_sum, min_end)

            _sum += n

        return max(max_sum, _sum - min_sum) if max_sum > 0 else max_sum
