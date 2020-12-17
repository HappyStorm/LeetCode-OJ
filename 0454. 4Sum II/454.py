class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        N, ab_sum, cd_sum = len(
            A), collections.Counter(), collections.Counter()
        for i in range(N):
            for j in range(N):
                ab_sum[A[i]+B[j]] += 1

        for i in range(N):
            for j in range(N):
                cd_sum[C[i]+D[j]] += 1

        ans = 0
        for s in ab_sum.keys():
            if -s in cd_sum:
                ans += ab_sum[s]*cd_sum[-s]
        return ans
