class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans, spec = [], A[0]
        for c in spec:
            if c in ans:
                continue

            ct, flag = spec.count(c), True
            for word in A[1:]:
                if c not in word:
                    flag = False
                    break

                ct = min(ct, word.count(c))

            if flag:
                ans += [c] * ct

        return ans