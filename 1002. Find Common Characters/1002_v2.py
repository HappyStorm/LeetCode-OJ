class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans, spec = [], A[0]
        for c in spec:
            ct, flag = [spec.count(c)], True
            for word in A[1:]:
                if c not in word:
                    flag = False
                    break

                ct += [word.count(c)]

            if flag and c not in ans:
                ans += [c] * min(ct)

        return ans