class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        idx_a, len_a, idx_b, len_b = 0, len(A), 0, len(B)
        while idx_a < len_a and idx_b < len_b:
            tmp_st = max(A[idx_a][0], B[idx_b][0])
            tmp_ed = min(A[idx_a][1], B[idx_b][1])

            if tmp_ed >= tmp_st:
                ans += [[tmp_st, tmp_ed]]

            if A[idx_a][1] > B[idx_b][1]:
                idx_b += 1

            else:
                idx_a += 1

        return ans
